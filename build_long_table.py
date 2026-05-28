"""
Wrangler para histone_ratios_nucleosoma_completo_para completar.txt

Entrada: TSV con 3 bloques horizontales (Ratio, Area, RT) x 34 muestras,
         34 columnas, 301 filas de datos. Anchor rows con formato
         'Peptide(Region)' marcan grupo; data rows formato 'Region modification'
         o 'Region peptide_variant' (caso H2A_1_7).

v4.0.0 (2026-05-26): join con phenodata_v4.csv para añadir batch + include_v4.
                     2 huérfanas técnicas excluidas (samples 6 y 28).

Salida: formato largo tidy con columnas:
  sample_index, sample_name, sample_code, sample_group,
  batch, date, include_v4,
  region, peptide, peptidoform, ratio, area, retention_time
"""

from __future__ import annotations
import re
import hashlib
from pathlib import Path
import pandas as pd

__version__ = "4.0.0"

INPUT = Path(r"C:/Users/geope/Downloads/histone_ratios_nucleosoma_completo_para completar.txt")
OUTDIR = Path(r"D:/AT_virgen/histone_long_table")
PHENODATA_V4 = OUTDIR / "phenodata_v4.csv"
OUTDIR.mkdir(parents=True, exist_ok=True)

# Embeber SHA256 del TXT crudo para trazabilidad (T2 v3.0.0 fix)
def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

INPUT_SHA256 = _sha256_file(INPUT)
print(f"[build_long_table v{__version__}] input SHA256 = {INPUT_SHA256[:16]}...")

# 1) lectura cruda
raw = pd.read_csv(INPUT, sep="\t", header=None, dtype=str, keep_default_na=False)
assert raw.shape == (303, 107), f"Forma inesperada: {raw.shape}"

# 2) cabeceras
hdr_samples = raw.iloc[0]
hdr_blocks  = raw.iloc[1]

# 3) muestras: parsear '1,2025017_10_AT_YNG'
sample_cols_ratio = list(range(3, 37))    # cols 3..36 = ratios 1..34
sample_cols_area  = list(range(38, 72))   # cols 38..71 = areas
sample_cols_rt    = list(range(73, 107))  # cols 73..106 = RT

def parse_sample_token(tok: str) -> dict:
    m = re.match(r"^(\d+),(\d{7})_(\d+)_AT_(\w+)$", tok)
    if not m:
        raise ValueError(f"Token de muestra mal formado: {tok!r}")
    idx, batch, biorep, group = m.groups()
    return {
        "sample_index": int(idx),
        "batch_id": batch,
        "sample_code": int(biorep),
        "sample_group": group,
        "sample_name": f"{batch}_{biorep}_AT_{group}",
    }

samples = [parse_sample_token(hdr_samples.iloc[c]) for c in sample_cols_ratio]
samples_df = pd.DataFrame(samples)
print(f"[OK] {len(samples_df)} muestras parseadas")
print(samples_df.groupby("sample_group").size().to_dict())

# coherencia: los 3 bloques deben tener exactamente las mismas etiquetas
for cols, label in [(sample_cols_area, "Area"), (sample_cols_rt, "RT")]:
    block_tokens = [hdr_samples.iloc[c] for c in cols]
    if block_tokens != [hdr_samples.iloc[c] for c in sample_cols_ratio]:
        raise RuntimeError(f"Bloque {label} no coincide con Ratio")

# 4) datos: filas 3..302 (0-indexed: 2..302)
data = raw.iloc[2:].reset_index(drop=True).copy()
data.columns = list(range(data.shape[1]))

# columnas semánticas
data = data.rename(columns={0: "_region_raw", 1: "_peptide_raw", 2: "peptidoform"})

# 5) identificar anchor rows (Peptidoform contiene '(' y ')')
anchor_mask = data["peptidoform"].str.contains(r"\(.+\)", regex=True, na=False)
anchors = data.loc[anchor_mask, ["peptidoform"]].copy()

def parse_anchor(p: str) -> tuple[str, str]:
    m = re.match(r"^(.+?)\((.+)\)$", p.strip())
    if not m:
        raise ValueError(f"Anchor no parseable: {p!r}")
    pep, reg = m.groups()
    return pep.strip(), reg.strip()

anchors[["peptide_anchor", "region_anchor"]] = anchors["peptidoform"].apply(
    lambda p: pd.Series(parse_anchor(p))
)
print(f"[OK] {len(anchors)} anchor rows encontradas; {anchors['region_anchor'].nunique()} regiones unicas")

# mapping region -> peptide (priorizando peptidos != 'unmod')
mapping = (
    anchors[anchors["peptide_anchor"] != "unmod"]
    .drop_duplicates("region_anchor")
    .set_index("region_anchor")["peptide_anchor"]
    .to_dict()
)

# 6) procesar data rows
data_rows = data.loc[~anchor_mask].copy()

def split_peptidoform(p: str) -> tuple[str, str]:
    """Devuelve (region, modification_or_variant)."""
    parts = p.split(" ", 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1]

data_rows[["region", "_tail"]] = data_rows["peptidoform"].apply(
    lambda p: pd.Series(split_peptidoform(p))
)

# peptide: regla en cascada
#   - si region esta en mapping -> mapping[region]
#   - si region == 'H2A_1_7' -> el _tail es la secuencia del peptido variante
#   - en otro caso -> NaN
def resolve_peptide(row) -> str:
    reg = row["region"]
    if reg == "H2A_1_7":
        return row["_tail"]
    return mapping.get(reg, "")

data_rows["peptide"] = data_rows.apply(resolve_peptide, axis=1)

# region no resuelta -> log
missing = data_rows[~data_rows["region"].isin(mapping) & (data_rows["region"] != "H2A_1_7")]
print(f"[OK] {len(data_rows)} data rows; {missing['region'].nunique()} regiones sin mapping")
if len(missing) > 0:
    print("  regiones sin mapping:", sorted(missing['region'].unique()))

# 7) extraccion de los 3 bloques numericos
def to_float(s: str):
    s = s.strip()
    if s == "" or s.lower() == "nan":
        return pd.NA
    try:
        return float(s)
    except ValueError:
        return pd.NA

def extract_block(df: pd.DataFrame, cols: list[int], value_name: str) -> pd.DataFrame:
    block = df.loc[:, cols].copy()
    block.columns = [s["sample_index"] for s in samples]
    block = block.apply(lambda col: col.map(to_float))
    block.insert(0, "_row_id", df.index)
    long = block.melt(id_vars="_row_id", var_name="sample_index", value_name=value_name)
    return long

long_ratio = extract_block(data_rows, sample_cols_ratio, "ratio")
long_area  = extract_block(data_rows, sample_cols_area,  "area")
long_rt    = extract_block(data_rows, sample_cols_rt,    "retention_time")

# 8) merge bloques + dimensiones
dims = data_rows[["region", "peptide", "peptidoform"]].copy()
dims["_row_id"] = data_rows.index

long = (
    long_ratio
    .merge(long_area, on=["_row_id", "sample_index"])
    .merge(long_rt,   on=["_row_id", "sample_index"])
    .merge(dims, on="_row_id")
    .merge(samples_df[["sample_index", "sample_name", "sample_code", "sample_group"]],
           on="sample_index")
    .drop(columns="_row_id")
)

# v4.0.0: JOIN con phenodata_v4 para añadir batch + include_v4 ------------
print(f"\n[v{__version__}] Joining with phenodata_v4.csv...")
ph_v4 = pd.read_csv(PHENODATA_V4)
print(f"  phenodata_v4: {len(ph_v4)} filas; "
      f"incluidas (include_v4=Yes): {(ph_v4['include_v4']=='Yes').sum()}")

ph_join = ph_v4[["sample_index", "batch", "date", "include_v4", "notes"]].copy()
long = long.merge(ph_join, on="sample_index", how="left")

# Validar: ninguna fila debe quedar sin batch tras el join
n_missing_batch = long["batch"].isna().sum()
if n_missing_batch > 0:
    raise RuntimeError(f"{n_missing_batch} filas sin batch tras join — phenodata incompleto")

# orden final de columnas v4.0.0
long = long[[
    "sample_index", "sample_name", "sample_code", "sample_group",
    "batch", "date", "include_v4", "notes",
    "region", "peptide", "peptidoform",
    "ratio", "area", "retention_time",
]].sort_values(["region", "peptidoform", "sample_index"]).reset_index(drop=True)

# Resumen del join
n_incl = (long["include_v4"] == "Yes").sum() // long["peptidoform"].nunique() \
    if long["peptidoform"].nunique() > 0 else 0
print(f"  samples include_v4=Yes en long table: {n_incl}")
print(f"  filas totales en long table: {len(long)}")

print(f"[OK] tabla larga: {long.shape}")
print(long.head(3).to_string())

# 9) export
csv_path  = OUTDIR / "histone_ratios_long.csv"
xlsx_path = OUTDIR / "histone_ratios_long.xlsx"
map_path  = OUTDIR / "region_peptide_mapping.csv"

# CSV (UTF-8 con BOM para Excel ES)
long.to_csv(csv_path, index=False, encoding="utf-8-sig")
pd.DataFrame(
    [{"region": r, "peptide": p} for r, p in sorted(mapping.items())]
).to_csv(map_path, index=False, encoding="utf-8-sig")

# XLSX con formato + tabla con autofiltro
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = Workbook()

# hoja 1: tabla larga
ws = wb.active
ws.title = "long_table"
for r in dataframe_to_rows(long, index=False, header=True):
    ws.append(r)

# tabla con estilo
last_col = get_column_letter(long.shape[1])
last_row = long.shape[0] + 1
tbl = Table(displayName="HistoneRatios", ref=f"A1:{last_col}{last_row}")
tbl.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium2", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=False
)
ws.add_table(tbl)

# autoanchos
for i, col in enumerate(long.columns, 1):
    width = max(len(str(col)), long[col].astype(str).str.len().clip(upper=40).max())
    ws.column_dimensions[get_column_letter(i)].width = min(int(width) + 2, 32)
ws.freeze_panes = "A2"

# hoja 2: dimensiones
ws2 = wb.create_sheet("samples")
for r in dataframe_to_rows(samples_df, index=False, header=True):
    ws2.append(r)
for cell in ws2[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="DCE6F1")
ws2.freeze_panes = "A2"

ws3 = wb.create_sheet("region_peptide_map")
mp = pd.DataFrame([{"region": r, "peptide": p} for r, p in sorted(mapping.items())])
for r in dataframe_to_rows(mp, index=False, header=True):
    ws3.append(r)
for cell in ws3[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="DCE6F1")
ws3.freeze_panes = "A2"

# hoja 4: schema/legend
ws4 = wb.create_sheet("README")
readme = [
    ["Campo", "Descripcion"],
    ["sample_index", "indice 1-34 segun orden de columna en fichero origen"],
    ["sample_name",  "nombre completo 2025017_<biorep>_AT_<grupo>"],
    ["sample_code",  "codigo biologico del replicate (entero entre _ _)"],
    ["sample_group", "grupo experimental: YNG, BOT, FLOR, SEN"],
    ["batch",        "v4.0.0: batch tecnico A (20250506) o B (20250507)"],
    ["date",         "v4.0.0: fecha de adquisicion MS (20250506 o 20250507)"],
    ["include_v4",   "v4.0.0: Yes/No - filtrar por include_v4=='Yes' antes de stats"],
    ["notes",        "v4.0.0: razon de exclusion si include_v4=='No'"],
    ["region",       "region peptidica (ej. H3_3_8, H4_4_17)"],
    ["peptide",      "secuencia del peptido canonico de la region"],
    ["peptidoform",  "forma peptidica con PTM o variante (ej. H3_3_8 K4me1)"],
    ["ratio",        "ratio relativo dentro del peptido (proporcion del area)"],
    ["area",         "area del pico cromatografico"],
    ["retention_time", "tiempo de retencion en minutos"],
    ["", ""],
    ["Notas:", ""],
    ["- 34 muestras", "YNG=5, BOT=10, FLOR=10, SEN=9 (ver hoja samples)"],
    ["- Anchor rows", "filas con 'Peptide(Region)' en fichero origen, usadas para mapping; excluidas del output"],
    ["- H2A_1_7", "caso especial: variantes naturales del peptido; el peptide se toma del propio peptidoform"],
    ["- Ceros", "valores 0 originales conservados (significan no detectado en esa muestra)"],
    ["- Decimales", "punto decimal (formato analitico estandar)"],
]
for r in readme:
    ws4.append(r)
ws4.column_dimensions["A"].width = 22
ws4.column_dimensions["B"].width = 90
for cell in ws4[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="DCE6F1")

wb.save(xlsx_path)

print(f"\n[OK] outputs en {OUTDIR}")
print(f"  - {csv_path.name}")
print(f"  - {xlsx_path.name}")
print(f"  - {map_path.name}")

# 10) QA summary
print("\n=== QA SUMMARY ===")
print(f"filas en long table       : {len(long):>8d}")
print(f"peptidoformas unicas      : {long['peptidoform'].nunique():>8d}")
print(f"regiones unicas           : {long['region'].nunique():>8d}")
print(f"peptides unicos (no vacio): {(long['peptide']!='').sum() // 34:>8d}")
print(f"muestras unicas           : {long['sample_name'].nunique():>8d}")
print(f"grupos                    : {sorted(long['sample_group'].unique())}")
print(f"ratio: NaN/total          : {long['ratio'].isna().sum()}/{len(long)}")
print(f"ratio: 0/total            : {(long['ratio']==0).sum()}/{len(long)}")
print(f"area:  NaN/total          : {long['area'].isna().sum()}/{len(long)}")
print(f"rt:    NaN/total          : {long['retention_time'].isna().sum()}/{len(long)}")
print(f"ratio min/max             : {long['ratio'].min():.4f} / {long['ratio'].max():.4f}")
print(f"area  min/max             : {long['area'].min():.4e} / {long['area'].max():.4e}")
print(f"rt    min/max             : {long['retention_time'].min():.2f} / {long['retention_time'].max():.2f}")
