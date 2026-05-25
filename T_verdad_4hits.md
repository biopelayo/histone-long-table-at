# Verdad numérica · 4 peptidoformas BH-FDR<0.05

**Fecha:** 2026-05-25
**Fuente:** `13_stats_pairwise.rds` (post-tar_make v3.0.0)
**Hedges:** `13c_bootstrap_hedges_ci.rds`

## Tabla canónica

| contrast | peptidoform | peptide | fdr_bh | p_value | log2fc | cohens_d |
|---|---|---|---|---|---|---|
| BOT_vs_SEN | H3_27_40 K27me2 | H3_27_40 | 0.01746 | 0.00036 | -1.142 | -2.148 |
| BOT_vs_SEN | H4_20_23 K20me1 | H4_20_23 | 0.01746 | 0.0003013 | 1.714 |  1.86 |
| BOT_vs_SEN | H3_27_40 unmod | H3_27_40 | 0.0351 | 0.001086 | 2.177 | 2.046 |
| BOT_vs_SEN | H4_20_23 K20me2 | H4_20_23 | 0.03599 | 0.001484 | -3.436 | -1.557 |

## Resumen por contraste

# A tibble: 1 × 2
  contrast       n
  <glue>     <int>
1 BOT_vs_SEN     4

## Decisión D-034 (propuesta)

Las 4 peptidoformas listadas son la **verdad canónica** para cap. 4 v3.1.0.
Cualquier prosa downstream debe usar exactamente esta tabla.
