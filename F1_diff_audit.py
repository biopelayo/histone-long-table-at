"""
F1 - Diff audit entre el fichero viejo (CAP4_NUEVO_INPUT/histone_ratios.txt)
y la nueva tabla maestra (histone_ratios_long.csv).

Output: dataset_diff_report.md con tres secciones:
  1. Diff de muestras (cuáles existen en cada uno)
  2. Diff de peptidoformas
  3. Diff de valores para peptidoformas comunes
"""
from __future__ import annotations
import re
from pathlib import Path
import pandas as pd
import numpy as np

OLD = Path("D:/CAP4_NUEVO_INPUT/histone_ratios.txt")
NEW_LONG = Path("D:/AT_virgen/histone_long_table/histone_ratios_long.csv")
OUTDIR = Path("D:/AT_virgen/histone_long_table")
REPORT = OUTDIR / "dataset_diff_report.md"


def parse_old_tsv(path: Path) -> tuple[pd.DataFrame, list[str]]:
    """Parser del TSV viejo (105 cols). Devuelve long-format y lista de samples."""
    raw = pd.read_csv(path, sep="\t", header=None, dtype=str, keep_default_na=False)
    ncols = raw.shape[1]
    print(f"  old file: {raw.shape}")

    # detectar bloques por columnas vacias en header (linea 0)
    hdr = raw.iloc[0].tolist()
    empty_idx = [i for i, v in enumerate(hdr) if v == "" and i > 0]
    # primer bloque empieza tras la primera col vacia consecutiva al inicio
    # mas simple: hay 3 bloques de samples; encontrar el primer "1,2025..."
    block_label_row = raw.iloc[1].tolist()
    # localizar inicios de cada bloque por etiqueta
    blocks: dict[str, list[int]] = {}
    current_label = None
    current_cols: list[int] = []
    for i, lab in enumerate(block_label_row):
        if lab in ("Ratio", "Area", "RT(min)"):
            if current_label != lab:
                if current_label is not None and current_cols:
                    blocks.setdefault(current_label, []).extend(current_cols)
                current_label = lab
                current_cols = [i]
            else:
                current_cols.append(i)
        else:
            if current_label is not None and current_cols:
                blocks.setdefault(current_label, []).extend(current_cols)
                current_label = None
                current_cols = []
    if current_label is not None and current_cols:
        blocks.setdefault(current_label, []).extend(current_cols)

    # samples (del primer bloque)
    samples = [hdr[c] for c in blocks["Ratio"]]
    print(f"  old samples: {len(samples)}")

    # parsear data rows
    rows = []
    current_peptide = None
    for ridx in range(2, raw.shape[0]):
        label = raw.iat[ridx, 0].strip() if raw.iat[ridx, 0] else ""
        if not label:
            # buscar peptidoform en col 2 (formato anchor: "TKQTAR(H3_3_8)")
            # algunas filas tienen label en col 0, otras en col 2
            label = raw.iat[ridx, 2].strip() if raw.shape[1] > 2 else ""
        if not label:
            continue
        if re.search(r"\(.+\)$", label):
            current_peptide = re.sub(r".*\(([^)]+)\)$", r"\1", label)
            continue
        if current_peptide is None:
            continue
        for c, sname in zip(blocks["Ratio"], samples):
            v = raw.iat[ridx, c].strip()
            ratio = float(v) if v else np.nan
            rows.append({
                "peptidoform": label,
                "sample": sname,
                "ratio": ratio,
            })
        # area + rt si quieres añadir luego
    df = pd.DataFrame(rows)
    return df, samples


def parse_new_long(path: Path) -> tuple[pd.DataFrame, list[str]]:
    df = pd.read_csv(path, encoding="utf-8-sig")
    samples = sorted(df["sample_name"].unique().tolist())
    return df, samples


def norm_sample(s: str) -> str:
    """Normaliza el id de muestra para comparar viejo vs nuevo.
    Viejo: '1,2025017_10_AT_YNG' o '2025017_10_AT_YNG'
    Nuevo: '2025017_10_AT_YNG'"""
    if "," in s:
        return s.split(",", 1)[1]
    return s


def main():
    print("[F1] parseando viejo...")
    old_df, old_samples = parse_old_tsv(OLD)
    print(f"  old long: {old_df.shape}, peptidoformas: {old_df['peptidoform'].nunique()}")

    print("[F1] cargando nuevo...")
    new_df, new_samples = parse_new_long(NEW_LONG)
    print(f"  new long: {new_df.shape}, peptidoformas: {new_df['peptidoform'].nunique()}")

    # normalizar samples
    old_samples_norm = sorted({norm_sample(s) for s in old_samples})
    new_samples_norm = sorted(new_samples)

    only_old_s = sorted(set(old_samples_norm) - set(new_samples_norm))
    only_new_s = sorted(set(new_samples_norm) - set(old_samples_norm))
    common_s = sorted(set(old_samples_norm) & set(new_samples_norm))

    # peptidoformas
    old_pf = set(old_df["peptidoform"].unique())
    new_pf = set(new_df["peptidoform"].unique())
    only_old_pf = sorted(old_pf - new_pf)
    only_new_pf = sorted(new_pf - old_pf)
    common_pf = sorted(old_pf & new_pf)

    # diff de valores para peptidoformas + muestras comunes
    old_df = old_df.assign(sample_norm=old_df["sample"].map(norm_sample))
    new_sub = new_df.rename(columns={"sample_name": "sample_norm"})[
        ["peptidoform", "sample_norm", "ratio"]
    ]
    merged = (
        old_df.rename(columns={"ratio": "ratio_old"})
        .merge(
            new_sub.rename(columns={"ratio": "ratio_new"}),
            on=["peptidoform", "sample_norm"],
            how="inner",
        )
    )
    merged["abs_diff"] = (merged["ratio_old"] - merged["ratio_new"]).abs()
    merged["rel_diff"] = merged["abs_diff"] / merged["ratio_old"].replace(0, np.nan)
    n_total = len(merged)
    n_exact = int((merged["abs_diff"] < 1e-6).sum())
    n_small = int(((merged["abs_diff"] >= 1e-6) & (merged["abs_diff"] < 1e-3)).sum())
    n_big = int((merged["abs_diff"] >= 1e-3).sum())

    # top discrepancias
    top_diff = merged.sort_values("abs_diff", ascending=False).head(20)

    # peptidoformas con cualquier discrepancia
    pf_with_diff = merged.loc[merged["abs_diff"] >= 1e-6, "peptidoform"].nunique()

    # escribir reporte
    lines = []
    A = lines.append
    A("# Diff Report · dataset viejo vs nueva tabla maestra")
    A("")
    A(f"**Fecha:** 2026-05-24  ")
    A(f"**Viejo:** `{OLD}`  ")
    A(f"**Nuevo (long):** `{NEW_LONG}`")
    A("")
    A("## 1. Muestras")
    A("")
    A(f"- Viejo: **{len(old_samples_norm)}** muestras únicas")
    A(f"- Nuevo: **{len(new_samples_norm)}** muestras únicas")
    A(f"- Comunes: **{len(common_s)}**")
    A(f"- Solo en viejo: **{len(only_old_s)}** → {only_old_s}")
    A(f"- Solo en nuevo: **{len(only_new_s)}** → {only_new_s}")
    A("")
    A("## 2. Peptidoformas")
    A("")
    A(f"- Viejo: **{len(old_pf)}** únicas")
    A(f"- Nuevo: **{len(new_pf)}** únicas")
    A(f"- Comunes: **{len(common_pf)}**")
    A(f"- Solo en viejo: **{len(only_old_pf)}**")
    A(f"- Solo en nuevo: **{len(only_new_pf)}**")
    if only_old_pf:
        A("")
        A("<details><summary>Peptidoformas que solo están en el viejo</summary>")
        A("")
        for pf in only_old_pf:
            A(f"- `{pf}`")
        A("")
        A("</details>")
    if only_new_pf:
        A("")
        A("<details><summary>Peptidoformas que solo están en el nuevo</summary>")
        A("")
        for pf in only_new_pf:
            A(f"- `{pf}`")
        A("")
        A("</details>")
    A("")
    A("## 3. Valores (ratios) en celdas comunes (peptidoforma × muestra)")
    A("")
    A(f"- Celdas comparadas: **{n_total}**")
    A(f"- Idénticas (|Δ|<1e-6): **{n_exact}** ({n_exact/n_total*100:.1f} %)")
    A(f"- Pequeñas (1e-6≤|Δ|<1e-3): **{n_small}** ({n_small/n_total*100:.1f} %)")
    A(f"- Grandes (|Δ|≥1e-3): **{n_big}** ({n_big/n_total*100:.1f} %)")
    A(f"- Peptidoformas con alguna discrepancia: **{pf_with_diff}** de {len(common_pf)}")
    A("")
    A("### Top 20 discrepancias por |Δ| absoluta")
    A("")
    A("| peptidoform | sample | ratio_old | ratio_new | |Δ| | rel_diff |")
    A("|---|---|---:|---:|---:|---:|")
    for _, r in top_diff.iterrows():
        rd = f"{r['rel_diff']:.4f}" if pd.notna(r["rel_diff"]) else "n/a"
        A(f"| `{r['peptidoform'][:40]}` | {r['sample_norm']} | {r['ratio_old']:.4f} | {r['ratio_new']:.4f} | {r['abs_diff']:.4f} | {rd} |")
    A("")
    A("## 4. Veredicto")
    A("")
    if n_exact == n_total:
        A("**Identidad perfecta** en celdas comunes. La diferencia entre ficheros es solo de cobertura (más samples y peptidoformas en el nuevo).")
    elif n_big == 0:
        A(f"**Cambios menores** (todos |Δ|<1e-3). Posible reproceso MS sin cambios de método.")
    else:
        A(f"**Cambios sustantivos** en {n_big} celdas. Probable reanálisis Skyline o cambio de método.")
    A("")
    A(f"- Muestra(s) extra en el nuevo: **{only_new_s}**")
    A(f"- Peptidoformas extra en el nuevo: **{len(only_new_pf)}**")
    A("")
    A("**Recomendación operativa:** la nueva tabla es la fuente correcta para v3.0.0. El input v2.0.0 queda como histórico.")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[F1] reporte escrito: {REPORT}")
    print(f"      celdas: {n_total} | exactas: {n_exact} | grandes: {n_big}")


if __name__ == "__main__":
    main()
