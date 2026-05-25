# Handoff v3.0.0 · Cap. 4 sobre tabla maestra refrescada

**Fecha:** 2026-05-25
**Sprint:** 9 fases ejecutadas en paralelo en una sola sesión.

## Lo que se hizo

| Fase | Output | Estado |
|---|---|---|
| F1 · Diff audit dataset viejo↔nuevo | `dataset_diff_report.md` | **HALLAZGO**: identidad numérica perfecta (9010/9010 celdas |Δ|<1e-6). Nuevo fichero = mismos valores, contenedor distinto. |
| F2 · Backup v2.0.0 frozen | `D:/CAP4_NUEVO_OUTPUT_v2.0.0_FROZEN/` (881 MB) | ✓ |
| F3 · Cargador R v3.0.0 | `R/01_load_raw.R` + `R/00_setup.R` (input_long_csv) + backup `.v2.0.0.bak` | Smoke test OK: 9010 filas, 34 muestras, 5+11+9+9, sanity Art. 16 ✓ |
| F4 · Design n=34 | sin cambios — `02_design.R` ya esperaba 5+11+9+9 | ✓ |
| F5 · Auditoría 28 scripts en 4 sub-agentes paralelos | `F5_audit_summary.md` | **TODOS APTOS** sin parches. 4 WARNINGS no bloqueantes documentadas. |
| F6 · `tar_make()` completo | `tar_make_v3_20260525_0909.log` | exit 0, 1m 27.8s, "1 completed, 40 skipped" (cache válida por F1) |
| F7 · Render cap. 4 v3.0.0 | `reports/cap4.html` + `.docx` + `.pdf` regenerados | ✓ |
| F8 · Tribunal Art. 16 (6 auditores paralelos) | `F8_tribunal_consolidado.md` | 6× APTO CON RESERVAS, riesgo agregado 25-30 % sin correcciones, ≤ 10 % con BLOQ-1..7 corregidos |
| F9 · Cierre + memoria | este documento + update MEMORY.md | ✓ |

## Decisiones nuevas adoptadas

- **D-025** El cargador del pipeline R lee la tabla maestra Python en lugar del TSV crudo (Opción B del master plan).
- **D-026** El TSV crudo queda archivado en `D:/CAP4_NUEVO_INPUT/` como evidencia histórica; no es input vivo del pipeline.
- **D-027** Backup v2.0.0 frozen en `D:/CAP4_NUEVO_OUTPUT_v2.0.0_FROZEN/` como referencia comparativa.
- **D-028** Sanity Art. 16 embebida en `01_load_raw.R` con 3 valores aleatorios verificados contra CSV maestro Python en cada ejecución.

## Hallazgo metodológico del sprint

El "data refresh" pedido por el usuario resultó ser un "container refresh": el fichero nuevo `histone_ratios_nucleosoma_completo_para completar.txt` y el viejo `histone_ratios.txt` codifican los **mismos 9010 valores numéricos** con dos columnas separadoras adicionales en el nuevo (107 vs 105). Por tanto:
- Las cifras del cap. 4 v2.0.0 (33 muestras, 97 peptidoformas, 4 BH-FDR<0.05) **se conservan exactamente** en v3.0.0.
- La discrepancia 34 vs 33 muestras es por `SAMPLES_TO_EXCLUDE = "6,2025017_15_AT_FLOR"` (la muestra del 81 % ceros).
- La discrepancia 265 vs 97 peptidoformas es por los filtros Garcia-lab encadenados (sensitivity, isobar, abundance, RT-CV, nonzero per group).

## Bloqueantes pendientes antes de defensa (consolidados del Tribunal)

1. **Reconciliar las 4 peptidoformas BH-FDR<0.05** entre `cap4.qmd` (FLOR-SEN) y `411_resumen.qmd` (BOT-SEN). Bloqueante absoluto.
2. **Crear repo público + tag v3.0.0 + DOI Zenodo**. CITATION.cff aún declara `2.0.0-cap4-final-pre-whisper`.
3. **Inicializar git en `D:/AT_virgen/histone_long_table/`** y versionar `build_long_table.py`.
4. **Editar título** "Atlas ontogénico" → "Panel descriptivo composicional" + `R/25_fig_workflow_cap4.R` Fig 4.10.
5. **Fig 4.7 stacked bars** debe usar `ptm_palette`, no la paleta ggplot2 por defecto.
6. **Consolidar bibliografía** en un único .bib con ≥65 entradas; añadir autocitas Pelayo/Valledor/Fraga.
7. **Reescribir cap. 3 §2.1.2** con lote 2025017 + n por estadio + DAS + variantes H2A.

## Entregables en `D:/AT_virgen/histone_long_table/`

```
build_long_table.py           ← generador Python idempotente
qa_audit.py                   ← validación cruzada de la tabla larga
F1_diff_audit.py              ← diff dataset viejo↔nuevo
histone_ratios_long.xlsx      ← tabla maestra (4 hojas + tabla con autofiltro)
histone_ratios_long.csv       ← tabla maestra (UTF-8 BOM)
region_peptide_mapping.csv    ← lookup 33 regiones → péptido canónico
dataset_diff_report.md        ← reporte F1
MASTER_PLAN.md                ← plan original v3.0.0
F5_audit_summary.md           ← auditoría 28 scripts R por 4 sub-agentes
F8_tribunal_consolidado.md    ← dictamen Art. 16 (6 capas, riesgo agregado)
FINAL_HANDOFF.md              ← este documento
QA_report.txt                 ← reporte QA del wrangler Python
```

## Próximo paso del usuario

Si Pelayo prioriza la defensa próxima:
- Ejecutar BLOQ-1, BLOQ-4 hoy (reconciliación 4 BH + título).
- Ejecutar BLOQ-2, BLOQ-5 esta semana (commit + repo público).
- Resto en sprint medio antes del envío al tribunal.

Si Pelayo prioriza la robustez del pipeline:
- BLOQ-3 (regenerar figs con timestamps frescos + nota en decisions.md).
- BLOQ-7 (cap. 3 reescritura): es el mayor coste pero el mayor beneficio.
- Sprint medio T1 (BCa bootstrap) y T2 (tests testthat + run_step hash de contenido).
