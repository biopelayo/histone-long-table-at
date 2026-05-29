# Handoff v4.0.1 · Cap. 4 prosa actualizada + Tribunal v4

**Fecha:** 2026-05-29
**Versión:** CAP4 v4.0.1 + histone_long_table v2.0.1

## OLA 15 ejecutada: 5 sub-agentes paralelos editando arsenal/_master/

| Sub-agente | Ficheros | Cambios |
|---|---|---|
| **A** | `46_inferencial.qmd`, `49_hallazgos.qmd` | Tabla canónica 9 hits, caveat YNG↔batch A x3, §4.6.1 renombrada |
| **B** | `41_datos.qmd`, `47_atlas.qmd` | 33→32, 97→99, §4.7.4 H2A reformulada con H2A_1_7 HVLLAVR top, §4.7.5 H2B reformulada con K4me3 |
| **C** | `410_discusion.qmd`, `4A_sensibilidad.qmd` | §4.10.7 nueva (batch correction), §4.A.14 nueva (sensitivity con/sin batch) |
| **D** | `capitulo4.qmd`, `40_intro.qmd`, `411_resumen.qmd`, `4E_glosario.qmd` | Frontmatter v4.0.0, resumen reescrito, 4 entradas nuevas glosario (batch, lm, ANOVA II, confounding) |
| **E** | `42`, `43`, `44`, `45`, `48`, `4B`, `4C`, `4D` | Barrido residual: 39 ediciones de cifras, +D-042..D-046 al 4C_decisiones |

## Tribunal v4 técnico (T1+T2+T3)

| Capa | v3.2.0 | v4.0.0 | v4.0.1 | Veredicto v4.0.1 |
|---|---:|---:|---:|---|
| T1 Estadística | 4 % | 4 % | **4 %** | APTO CON RESERVAS |
| T2 Reproducibilidad | 5 % | 6 % | **5 %** ↓ | APTO CON RESERVAS (tests cerrados) |
| T3 Prosa | 5 % | 3 % | **3 %** | **APTO PARA TRIBUNAL** |

**Riesgo agregado v4.0.1: 4-5 %** (vs 5-7 % v3.2.0).

## Cambios v4.0.1 (post Tribunal v4)

1. **Tests testthat actualizados** a v4.0.0:
   - `test-01_load_raw.R`: 9010→8480 filas, 34→32 muestras, distribución 5+11+8+8, samples 6 y 28 excluidos, factor batch A/B en sample_design_v4
   - `test-cardinality-post-filter.R`: 33→32 muestras, 97→99 PF, cross-tab condición×batch validado, 9 hits BH-FDR<0.05 con verdad canónica D-046

2. **Soporte bundle peptidos flexible** (preparación post-Tribunal revision_peptidos v5):
   - `01_load_raw.R`: rango 200-320 PF aceptado; `nrow = 32 × n_pf` dinámico
   - `build_long_table.py`: shape filas 270-350 aceptado (era 303 fijo)
   - Backup `build_long_table.py.bak_pre_v5_20260528_171943`

3. **D-042..D-046 documentadas** en `arsenal/_master/sections/4C_decisiones.qmd` como entradas formales del log.

## Pendientes

### Inmediato (próxima sesión)
1. **Render cap. 4 master arsenal**: los sub-agentes editaron `D:/Antigravity/arsenal/_master/sections/*.qmd`, pero `99_render_report.R` renderiza `D:/CAP4_NUEVO_OUTPUT/reports/cap4.qmd` (monolítico, contenido propio). Hay que decidir:
   - (a) Sincronizar arsenal → reports (copia masiva)
   - (b) Renderizar el master arsenal directamente con quarto (probablemente la vía cleaner)
2. **Sensitivity sin YNG** en §4.A: 5 contrastes pareados sin confounding YNG↔batch A (Tribunal T1 W2).
3. **Homogeneizar 13d**: cambiar de `summary.lm` a `emmeans + vcovHC HC3` para coherencia con 12c (T1 W3).

### Diferido post-defensa
- Render figuras desde arsenal (algunas captions aún dicen "33 muestras" en `figures/`).
- Aplicar Tribunal Art. 16 v4 con 6 capas (sólo se hicieron T1+T2+T3 esta sesión).
- DOI Zenodo definitivo.
- Migración APA→@key completa.
- Autocitas Valledor/Fraga.

## Tags y push

- **CAP4**: `v4.0.0` + `v4.0.1` push a `github.com/biopelayo/cap4-histone-ptms-at`
- **histone_long_table**: `v2.0.0` + `v2.0.1` push a `github.com/biopelayo/histone-long-table-at`

## Estado de los repos

```
D:/CAP4_NUEVO_OUTPUT/        ← HEAD = v4.0.1, main pushed, clean
D:/AT_virgen/histone_long_table/  ← HEAD = v2.0.1, master pushed, clean
D:/Antigravity/arsenal/_master/   ← NO ES git repo (changes locales)
```

## Resumen del viaje completo (cap. 4 v2.0.0 → v4.0.1)

| Versión | Hito | Cambio nuclear |
|---|---|---|
| v2.0.0 | Inicial pre-Tribunal | 33 muestras, 97 PF, 4 hits BOT-SEN |
| v3.0.0 | Cap. 4 sobre tabla maestra refrescada | F1 demostró identidad, contenedor cambia |
| v3.1.0 | Sprint nivel dios cierre 7 bloqueantes | Tribunal Art. 16, 25→12% riesgo |
| v3.2.0 | Cierre riesgo mínimo | Repo público, BCa, IHW, DOIs verificados, 5-7% riesgo |
| **v4.0.0** | **Phenodata corregido + batch** | **2 huérfanas excluidas, batch real A/B, 9 hits en 3 contrastes** |
| **v4.0.1** | **OLA 15 + Tribunal v4 + tests v4** | **Prosa actualizada, riesgo 4-5%** |

Hits canónicos v4.0.1 (D-046):
- **BOT_vs_SEN** (4): H2A_1_7 HVLLAVR (TOP, g=-1.75), H3_27_40 K27me2 (g=-2.27), H3_27_40 unmod (g=+2.41), H4_20_23 K20me1 (g=+2.25)
- **BOT_vs_FLOR** (1): H2B7_311_disc K4me3 (g=-1.50)
- **YNG_vs_SEN** (4): H3_3_8 K4me1/unmod, H33_27_40 K27me1K36me2, H3_27_40 K27me1K36me3

H4_20_23 K20me2 desaparece al controlar batch (era hit en v3.2.0).
