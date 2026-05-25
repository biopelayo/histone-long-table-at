# histone_long_table

Tabla maestra tidy en formato largo derivada de los datos de proteómica histonas del lote **2025017** (*Arabidopsis thaliana*, hPTMs, 4 estadios YNG/BOT/FLOR/SEN).

## Propósito

Convertir el TSV crudo de Skyline (`histone_ratios_nucleosoma_completo_para completar.txt`, 107 cols × 303 filas con 3 bloques horizontales Ratio/Area/RT y celdas combinadas) en una tabla larga tidy de **9010 filas × 10 columnas** que sirve de contrato de datos para el pipeline R/targets del cap. 4 de la tesis.

## Contenido

| Fichero | Descripción |
|---|---|
| `build_long_table.py` | Generador idempotente del CSV/XLSX maestro |
| `qa_audit.py` | Validación cruzada (sanity vs raw, ratios suman ~1 por péptido) |
| `F1_diff_audit.py` | Comparación dataset viejo↔nuevo |
| `OLA1_verdad_numerica.R` | Extracción de las 4 peptidoformas BH-FDR<0.05 |
| `histone_ratios_long.xlsx` | Tabla maestra (4 hojas con autofiltro) |
| `histone_ratios_long.csv` | Tabla maestra UTF-8 BOM |
| `region_peptide_mapping.csv` | Lookup canónico 33 regiones → péptido |
| `T_verdad_4hits.{csv,md}` | Verdad canónica de las 4 peptidoformas BH-FDR<0.05 |
| `dataset_diff_report.md` | Reporte F1 (identidad numérica perfecta vs v2.0.0) |
| `F5_audit_summary.md` | Auditoría 28 scripts R por 4 sub-agentes |
| `F8_tribunal_consolidado.md` | Dictamen Art. 16 v3.0.0 (6 capas) |
| `MASTER_PLAN.md` | Plan inicial v3.0.0 |
| `MASTER_PLAN_v3.1.0.md` | Plan extendido v3.1.0 con 8 olas |
| `FINAL_HANDOFF.md` | Handoff del sprint v3.0.0 |
| `QA_report.txt` | Reporte QA del wrangler |

## Schema de la tabla larga

```
sample_index    int    1..34 (orden de columna en TSV origen)
sample_name     str    2025017_<biorep>_AT_<grupo>
sample_code     int    biological replicate (1..34, no ordenado)
sample_group    str    YNG | BOT | FLOR | SEN
region          str    H3_3_8, H4_4_17, etc. (33 regiones)
peptide         str    KSTGGKAPR, TKQTAR, etc.
peptidoform     str    H3_3_8 K4me1, H4_4_17 K12acK16ac, etc.
ratio           float  proporción intra-péptido (0..1)
area            float  área del pico cromatográfico
retention_time  float  RT en minutos
```

## Cardinalidad

- **34 muestras**: BOT=11, FLOR=9, SEN=9, YNG=5
- **265 peptidoformas** pre-filtrado, **97** post-filtrado Garcia-lab
- **33 regiones**, **40 péptidos canónicos**

## Reproducibilidad

```bash
# Generar tabla larga desde el TSV crudo
python build_long_table.py

# Validar
python qa_audit.py

# Extraer verdad numérica (requiere pipeline R en D:/CAP4_NUEVO_OUTPUT/)
cd D:/CAP4_NUEVO_OUTPUT && Rscript D:/AT_virgen/histone_long_table/OLA1_verdad_numerica.R
```

## Versiones

- **v1.0.0** (2026-05-25): release inicial con sprint v3.0.0 + Tribunal Art. 16 + OLA 1.

## Contrato downstream

El pipeline `D:/CAP4_NUEVO_OUTPUT/R/01_load_raw.R` v3.0.0 consume `histone_ratios_long.csv` como única fuente de datos.

## Licencia

GPL-3.0 (alineado con la tesis).

## Autoría

Pelayo González de Lena Rodríguez (UniOvi). Cotutela: Mario Fraga, Luis Valledor.
