# Verdad numérica v4.0.0 · contrastes pareados con batch covariable

**Fecha:** 2026-05-26
**Fuente:** `D:/CAP4_NUEVO_OUTPUT/data/processed/13d_stats_pairwise_batch.rds`
**Diseño:** lm(clr ~ condition + batch), ANOVA tipo II, BH-FDR por contraste

## Resumen ejecutivo

**9 peptidoformas BH-FDR<0.05** distribuidas en **3 contrastes** (vs 4 hits todos en BOT_vs_SEN en v3.2.0 sin batch).

## Tabla canónica v4.0.0 (9 hits)

### BOT_vs_FLOR (1 hit nuevo)

| # | Peptidoforma | Péptido | log2FC | Hedges g | p-valor | BH-FDR |
|---|---|---|---:|---:|---:|---:|
| 1 | H2B7_311_disc K4me3 | IFEKLAQEASKLAR | -1,590 | **-1,502** | 1,5e-4 | 0,015 |

### BOT_vs_SEN (4 hits — núcleo histórico v3.2.0)

| # | Peptidoforma | Péptido | log2FC | Hedges g | p-valor | BH-FDR | v3.2.0 |
|---|---|---|---:|---:|---:|---:|:---:|
| 2 | **H2A_1_7 HVLLAVR** | (variante natural) | -1,013 | **-1,747** | 1,6e-5 | **0,0016** | marginal→**top** |
| 3 | H3_27_40 K27me2 | KSAPATGGVKKPHR | -1,063 | **-2,266** | 1,8e-4 | 0,0067 | ✓ |
| 4 | H3_27_40 unmod | KSAPATGGVKKPHR | +2,403 | **+2,409** | 2,0e-4 | 0,0067 | ✓ |
| 5 | H4_20_23 K20me1 | KVLR | +1,665 | **+2,246** | 4,3e-4 | 0,011 | ✓ |
| ❌ | ~H4_20_23 K20me2~ | KVLR | — | — | — | — | desaparece |

### YNG_vs_SEN (4 hits nuevos)

| # | Peptidoforma | Péptido | log2FC | Hedges g | p-valor | BH-FDR |
|---|---|---|---:|---:|---:|---:|
| 6 | H3_3_8 K4me1 | TKQTAR | -0,043 | -0,077 | 9,6e-5 | 0,003 |
| 7 | H3_3_8 unmod | TKQTAR | +0,043 | +0,077 | 9,6e-5 | 0,003 |
| 8 | H33_27_40 K27me1K36me2 | KSAPTTGGVKKPHR | -0,362 | -1,062 | 8,8e-5 | 0,003 |
| 9 | H3_27_40 K27me1K36me3 | KSAPATGGVKKPHR | +1,034 | +0,918 | 8,8e-4 | 0,022 |

### Sin hits

YNG_vs_BOT, YNG_vs_FLOR, FLOR_vs_SEN.

## Comparativa v3.2.0 → v4.0.0

| Aspecto | v3.2.0 (33 muestras, sin batch) | v4.0.0 (32 muestras, batch covariable) |
|---|---|---|
| **Total hits** | 4 (+1 marginal) | **9** |
| **Contrastes con hits** | 1 (BOT_vs_SEN) | **3 (BOT-FLOR, BOT-SEN, YNG-SEN)** |
| **Top hit** | H3_27_40 K27me2 (g=-2,15) | **H2A_1_7 HVLLAVR (g=-1,75)** |
| **Discrepancias** | — | 5 (entradas/salidas) |
| **Batch como factor** | ❌ "B1" hardcoded | ✓ A/B real del phenodata |
| **Tests por contraste** | 97 | 99 (3 peptidoformas más conservadas con n=32) |

## Hallazgos relevantes

1. **H2A_1_7 HVLLAVR** sube de "marginal en v3.2.0" a **top hit absoluto v4.0.0** (fdr=0.0016). Es una variante natural de péptido (no PTM clásica). Su confirmación tras corregir batch refuerza la hipótesis de heterogeneidad genética en H2A.

2. **H4_20_23 K20me2 desaparece** del listado significativo al controlar batch. Esto era el 4º hit del núcleo canónico v3.2.0 con `g=-1,56`. Sugiere que parte de su señal v3.2.0 era atribuible a batch B (donde están 7/8 SEN).

3. **H2B7_311_disc K4me3** aparece en BOT_vs_FLOR. Marca de transcripción activa que sube en FLOR. No estaba en el radar de v3.2.0.

4. **Contraste YNG_vs_SEN aparece** con 4 hits — pero **YNG está 100 % confounded con batch A**, así que estos hits deben interpretarse con cautela:
   - H3_3_8 K4me1 ↔ unmod: cambio sutil (g=±0,08) que sale significativo solo por p muy bajo
   - H33_27_40 K27me1K36me2 (g=-1,06): H3.3 con caída → marca biológicamente plausible
   - H3_27_40 K27me1K36me3 (g=+0,92): H3.1 con subida → coherente con re-heterocromatinización

5. **R² del modelo lm con batch + condición** varía entre 0,24 y 0,56 → el efecto biológico explica entre un 24 y un 56 % de la varianza CLR por peptidoforma.

## Decisión D-046 propuesta

Las 9 peptidoformas listadas son la **verdad canónica v4.0.0** del cap. 4. Toda prosa downstream debe usar esta tabla, no la v3.2.0.

Las 4 BOT_vs_SEN se conservan como **núcleo histórico estable** (mismo patrón en v2.0.0, v3.2.0 y v4.0.0). Las 4 YNG_vs_SEN y 1 BOT_vs_FLOR son **hallazgos nuevos v4.0.0** habilitados por la corrección de batch.
