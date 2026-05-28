# Handoff v4.0.0 · Cap. 4 con phenodata corregido + batch covariable

**Fecha:** 2026-05-26
**Estado:** datos y stats cerrados. Cap. 4 prosa pendiente de reescritura (OLA 15).

## El cambio nuclear de v4.0.0

**Phenodata corregido**: 32 muestras válidas (no 34), 2 batches reales (20250506 vs 20250507). Las etiquetas YNG/BOT/FLOR/SEN del TSV crudo SÍ eran correctas — lo que faltaba era el **batch técnico real**.

**Inferencia con batch covariable**: `lm(clr ~ condition + batch)` ANOVA tipo II.

## Verdad canónica v4.0.0 (9 hits BH-FDR<0.05)

### Núcleo histórico BOT_vs_SEN (4 hits, estable desde v2.0.0)
1. **H2A_1_7 HVLLAVR** (g=-1.75, fdr=0.0016) ← top hit v4.0.0
2. H3_27_40 K27me2 (g=-2.27, fdr=0.0067)
3. H3_27_40 unmod (g=+2.41, fdr=0.0067)
4. H4_20_23 K20me1 (g=+2.25, fdr=0.011)

### Hallazgos nuevos v4.0.0 (5 hits, antes ocultos por batch)
5. BOT_vs_FLOR: **H2B7_311_disc K4me3** (g=-1.50, fdr=0.015)
6. YNG_vs_SEN: H3_3_8 K4me1 (g=-0.08, fdr=0.003)
7. YNG_vs_SEN: H3_3_8 unmod (g=+0.08, fdr=0.003)
8. YNG_vs_SEN: H33_27_40 K27me1K36me2 (g=-1.06, fdr=0.003)
9. YNG_vs_SEN: H3_27_40 K27me1K36me3 (g=+0.92, fdr=0.022)

### Perdido vs v3.2.0
- H4_20_23 K20me2 — desaparece al controlar batch (era el 4º del núcleo)

## OLAs completadas

| OLA | Descripción | Resultado |
|---|---|---|
| 10 | Phenodata v4 desde cero | 32 muestras, 2 huérfanas técnicas (samples 6+28), cuadre perfecto con oficial |
| 11 | Rebuild build_long_table.py v4.0.0 | CSV largo 9010×14 con batch+include_v4 |
| 12 | 01_load_raw.R + 02_design.R adaptados | Cargador filtra include_v4; design con factor batch A/B |
| 13 | Batch correction + PCA pre/post | `Fig_4_10b_PCA_pre_post_batch.png`. R² PC1 batch: 0.128→0.069. β batch B: 2.93→0 |
| 14 | Stats con batch covariable | `R/12c_stats_lm_batch.R` (6 hits ómnibus), `R/13d_stats_pairwise_batch.R` (9 hits pareados) |
| 15 | Cap. 4 v4.0.0 reescrito | **PENDIENTE** — requiere re-redactar §4.7-4.11 con los 9 hits |

## Cross-tab condición × batch (confounding crítico)

```
       A    B
  YNG  5    0   ← 100% confounded con A
  BOT  5    6
  FLOR 2    6
  SEN  1    7   ← 87.5% en B
```

**Caveat**: hits YNG_vs_* deben interpretarse con cautela. El modelo `lm` los estima vía variabilidad batch en otros grupos.

## Decisiones nuevas (D-042..D-046)

Documentadas en `D:/CAP4_NUEVO_OUTPUT/docs/decisions.md`.

## Entregables v4.0.0

```
D:/AT_virgen/histone_long_table/
├── phenodata_v4_oficial.tsv          ← phenodata canónico (32 muestras)
├── phenodata_v4.csv                  ← v4 con include_v4 Yes/No (34 filas)
├── OLA10_phenodata_v4.R              ← script de cruce
├── OLA10_decidir_huerfana_SEN.R      ← QA objetivo para huérfana SEN A
├── OLA10_fix_huerfana_y_validar.R    ← cierre cuadre 32==32
├── T_verdad_4hits_v4.md              ← verdad canónica 9 hits
└── FINAL_HANDOFF_v4.0.0.md           ← este documento

D:/CAP4_NUEVO_OUTPUT/
├── R/01_load_raw.R                   ← v4.0.0 con include_v4 filter
├── R/02_design.R                     ← v4.0.0 con factor batch A/B
├── R/03_qc_pre_filter.R              ← expected_python actualizado (D-041 → D-046)
├── R/00_setup.R                      ← SAMPLES_TO_EXCLUDE = character(0)
├── R/10b_pca_batch_check.R           ← NEW: limma + PCA pre/post
├── R/12c_stats_lm_batch.R            ← NEW: Welch ANOVA + batch covariable
├── R/13d_stats_pairwise_batch.R      ← NEW: lm pareados + batch
├── output/figures/Fig_4_10b_PCA_pre_post_batch.{png,pdf}  ← NUEVA figura
├── data/processed/12c_stats_lm_batch.rds                  ← 6 hits ómnibus
├── data/processed/13d_stats_pairwise_batch.rds            ← 9 hits pareados
└── data/processed/10b_clr_batch_corrected.rds             ← CLR limma-corrected
```

## Próximo movimiento (OLA 15)

Reescritura del cap. 4 v4.0.0:

1. **§4.6 Inferencial**: actualizar a 9 hits, separar 4 estables BOT_vs_SEN del núcleo histórico + 5 nuevos habilitados por batch correction.
2. **§4.7 Atlas**: incluir H2A_1_7 HVLLAVR como top hit con interpretación de variante natural.
3. **§4.7.2 H2B7 K4me3**: sección nueva sobre BOT→FLOR (transcripción activa).
4. **§4.9 Hallazgos**: reorganizar con las 3 transiciones (BOT-FLOR, BOT-SEN, YNG-SEN) en lugar de solo BOT-SEN.
5. **§4.10 Discusión**: nueva sección "Efecto del batch técnico y su corrección".
6. **§4.A.X Sensibilidad**: comparativa de hits con/sin batch (5 discrepancias).
7. **Cifras a actualizar globalmente**: 33→32, 97→99, 4 hits→9 hits.

Estimación: 4-6 h. Cap. 3 ya está actualizado con DAS y EpiProfile-PLANTS desde v3.2.0.

## Pendientes post-defensa

- Aplicar Tribunal Art. 16 v4 (6 capas).
- Tag v4.0.0 en repos públicos GitHub.
- DOI Zenodo.
- Migración APA→@key completa.
- Autocitas Valledor/Fraga.
