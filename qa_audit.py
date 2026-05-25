"""Auditoria QA cruzada del output vs fichero origen."""
from pathlib import Path
import re
import pandas as pd

OUTDIR = Path(r"D:/AT_virgen/histone_long_table")
INPUT  = Path(r"C:/Users/geope/Downloads/histone_ratios_nucleosoma_completo_para completar.txt")

long = pd.read_csv(OUTDIR / "histone_ratios_long.csv", encoding="utf-8-sig")
raw  = pd.read_csv(INPUT, sep="\t", header=None, dtype=str, keep_default_na=False)

print("="*70)
print("AUDIT 1 - INTEGRIDAD DE DIMENSIONES")
print("="*70)
print(f"shape long table       : {long.shape}")
print(f"shape esperado         : (265*34=9010, 10)")
print(f"sample_name unicos     : {long['sample_name'].nunique()}  (esperado 34)")
print(f"peptidoform unicos     : {long['peptidoform'].nunique()}  (esperado 265)")
print(f"region unicos          : {long['region'].nunique()}")
print(f"peptide unicos         : {long['peptide'].nunique()}")
print(f"duplicados (sample+pep): {long.duplicated(['sample_name','peptidoform']).sum()}  (esperado 0)")

print()
print("="*70)
print("AUDIT 2 - DISTRIBUCION POR GRUPO")
print("="*70)
g = long.groupby("sample_group")["sample_name"].nunique()
print(g.to_string())
print(f"total samples: {g.sum()}")

print()
print("="*70)
print("AUDIT 3 - RANGOS Y CALIDAD POR BLOQUE")
print("="*70)
for col in ["ratio", "area", "retention_time"]:
    s = long[col]
    print(f"{col:>15s}: min={s.min():>10.4f} | max={s.max():>14.4f} | mean={s.mean():>12.4f} | nan={s.isna().sum():>4d} | zeros={(s==0).sum():>5d}")

print()
print("="*70)
print("AUDIT 4 - SANITY CHECK: 5 VALORES ALEATORIOS vs FICHERO ORIGEN")
print("="*70)
# tomar 5 filas no-cero al azar y verificar
import random
random.seed(42)
non_zero = long[long["ratio"] > 0].sample(5, random_state=42)
for _, row in non_zero.iterrows():
    pf = row["peptidoform"]
    sn = row["sample_name"]
    si = row["sample_index"]
    r  = row["ratio"]
    a  = row["area"]
    rt = row["retention_time"]
    # localizar en raw
    raw_row_idx = None
    for i in range(2, raw.shape[0]):
        if raw.iloc[i, 2] == pf:
            raw_row_idx = i
            break
    if raw_row_idx is None:
        print(f"  [FAIL] peptidoform '{pf}' no encontrada en raw")
        continue
    raw_ratio = raw.iloc[raw_row_idx, 2 + si]      # cols 3..36
    raw_area  = raw.iloc[raw_row_idx, 37 + si]     # cols 38..71
    raw_rt    = raw.iloc[raw_row_idx, 72 + si]     # cols 73..106
    def f(x): return float(x) if x.strip() else None
    ok = (abs(f(raw_ratio)-r) < 1e-6 and
          abs(f(raw_area)-a)  < 1e-3 and
          abs(f(raw_rt)-rt)   < 1e-3)
    flag = "OK" if ok else "FAIL"
    print(f"  [{flag}] {pf[:30]:30s} | s={sn:25s} | r={r:.4f}/{raw_ratio:>10s} | a={a:.2e}/{raw_area:>14s} | rt={rt:.2f}/{raw_rt:>6s}")

print()
print("="*70)
print("AUDIT 5 - TOTALES POR REGION (sanity de ratios)")
print("="*70)
# para cada (region, sample) los ratios deben sumar ~1 (proporciones)
sums = (long.groupby(["region", "sample_name"])["ratio"].sum()
        .reset_index().rename(columns={"ratio": "ratio_sum"}))
print(f"ratio_sum stats: min={sums['ratio_sum'].min():.4f} | "
      f"max={sums['ratio_sum'].max():.4f} | "
      f"mean={sums['ratio_sum'].mean():.4f}")
print(f"regiones con sum < 0.5 en alguna muestra:")
prob = sums[sums["ratio_sum"] < 0.5]
print(f"  {len(prob)} casos de {len(sums)}")
if len(prob) > 0:
    print(prob.groupby("region").size().sort_values(ascending=False).head(10).to_string())

print()
print("="*70)
print("AUDIT 6 - PEPTIDOFORMS POR REGION")
print("="*70)
print(long.groupby("region")["peptidoform"].nunique().sort_values(ascending=False).to_string())

print()
print("="*70)
print("AUDIT 7 - MUESTRAS PROBLEMATICAS (alto % de ceros)")
print("="*70)
zero_pct = (long.assign(is_zero=lambda d: d["ratio"]==0)
            .groupby("sample_name")["is_zero"].mean()
            .sort_values(ascending=False))
print("top 10 muestras con mas % de ceros en ratio:")
print((zero_pct.head(10)*100).round(1).to_string())

# guardar reporte
with open(OUTDIR / "QA_report.txt", "w", encoding="utf-8") as f:
    f.write("QA report generado por qa_audit.py\n")
    f.write(f"long table shape: {long.shape}\n")
    f.write(f"samples: {long['sample_name'].nunique()}\n")
    f.write(f"peptidoforms: {long['peptidoform'].nunique()}\n")
    f.write(f"regions: {long['region'].nunique()}\n")
    f.write(f"\nGrupos:\n{g.to_string()}\n")
    f.write(f"\nRatio sum stats por (region,sample):\n{sums['ratio_sum'].describe().to_string()}\n")
print(f"\n[OK] QA_report.txt escrito en {OUTDIR}")
