# Tribunal Art. 16 v3.0.0 · Dictamen consolidado

**Fecha:** 2026-05-25
**Sesión:** 6 auditores paralelos sobre v3.0.0 tras `tar_make()` exit 0.

## Veredicto global

| Capa | Veredicto | Riesgo % | Bloqueantes |
|---|---|---:|---:|
| T1 · Correctitud estadística | APTO CON RESERVAS | 9 % | 3 |
| T2 · Reproducibilidad | APTO CON RESERVAS | 12 % | 3 |
| T3 · Prosa académica + anti-AI-writing | APTO CON RESERVAS | 9 % | 3 |
| T4 · Figuras + Sistema Visual Pelamovic | APTO CON RESERVAS | 12 % | 3 |
| T5 · Coherencia cap. 3 ↔ cap. 4 | APTO CON RESERVAS | 6 % | 8 |
| T6 · Literatura | APTO CON RESERVAS | 14 % | 2 |

**Riesgo agregado (sin correcciones):** 25-30 % de no cum laude.
**Riesgo agregado (con BLOQ-1..BLOQ-7 corregidos):** ≤ 10 %.

## Bloqueantes que cruzan dos o más capas

**BLOQ-1 · Inconsistencia material en las 4 peptidoformas BH-FDR<0.05** (T3 + T5)
- `cap4.qmd` v2.0.0 línea 313: transición FLOR-SEN, 3 H4 acetiladas + 1 H3 K9me2.
- `411_resumen.qmd` v1.0.0 línea 11: transición BOT-SEN, H3_27_40 K27me2, H4_20_23 K20me1, H3_27_40 unmod, H4_20_23 K20me2.
- Discrepancia detectable por el tribunal en 5 minutos. Reconciliar contraste y nombres antes de defender. **Bloqueante absoluto.**

**BLOQ-2 · Repositorio sin sede pública** (T2)
- `git remote -v` vacío; FAIR violado.
- 12 ficheros modificados + 9 untracked sin commitear; CITATION.cff aún declara `2.0.0-cap4-final-pre-whisper`, no v3.0.0.
- Crear repo público (GitHub/Zenodo), tag firmado v3.0.0, DOI.

**BLOQ-3 · Figuras desfasadas a 2026-05-11** (T4)
- `tar_make()` v3.0.0 mostró "1 completed, 40 skipped". Las figuras no se regeneraron porque sus dependencias upstream tienen mismo hash (F1 confirma igualdad numérica).
- Aceptable epistemológicamente, pero exige documentar en `docs/decisions.md` que la invariancia de figuras es consecuencia de la igualdad de datos. Sin nota explícita, el tribunal lo lee como inconsistencia.

**BLOQ-4 · "Atlas" hardcodeado en Fig 4.10 y título** (T3 + T4)
- Decisión 2026-05-11 reformuló "Atlas ontogénico" → "Panel descriptivo composicional".
- `R/25_fig_workflow_cap4.R` líneas 33 y 41 contienen "Atlas".
- Título de `capitulo4.qmd` v1.0.0 mantiene "Atlas ontogénico".
- Editar y regenerar Fig 4.10 + reescribir título.

**BLOQ-5 · Generador Python `build_long_table.py` sin versionar** (T2)
- `D:/AT_virgen/histone_long_table/` no es repo Git.
- El CSV maestro puede cambiar silenciosamente.
- Inicializar git, versionar, embeber `__version__` en stdout y CSV.

**BLOQ-6 · Bibliografía con tres numeraciones distintas** (T6)
- Master declara ~70 entradas, `references.bib` tiene 33, sección "Referencias" del cap4.qmd lista 27.
- Cero autocitas Pelayo/Valledor/Fraga.
- Faltan: Lochmanová 2019/2024×2, Bourbousse 2012, Sidoli 2014, Sidoli & Garcia 2017, Hedges 1981, Gloor 2017, Lovell 2015, Wilkinson 2016.

**BLOQ-7 · Cap. 3 en estado borrador** (T5)
- Notas embebidas del codirector LV, tablas con numeración rota ("Table 245"), secciones placeholder.
- Lote 2025017 sin descripción, n por estadio no documentado, DAS por estadio ausente.
- Nomenclatura H2A (H2A_X, H2A.W6, etc.) no definida en cap. 3 pero usada intensivamente en cap. 4.

## Hallazgos sustantivos por capa

### T1 Estadística
- Bootstrap percentil para Hedges *g* con n=5 (YNG): cambiar a BCa o documentar comparación percentil-basic en los 4 hits BH.
- BH-FDR por contraste = familia separada: defendible (BH 1995 §3) pero requiere justificación explícita en cap. 4.
- 21_plsda.R: validación LOO sobre grupos desbalanceados (5-11) honesta solo si se reporta BER, no accuracy.
- 16 ANOVA clásico vs 16b Welch: promover 16b a primario para coherencia con D-022.

### T2 Reproducibilidad
- Rutas D:/ hardcoded en `00_setup.R`. Migrar a `Sys.getenv()`.
- `run_step()` hashea size+mtime de rds, no contenido. Cambiar a `digest::digest(file=..., algo="xxhash64")`.
- Añadir `tar_target(input_csv, paths$input_long_csv, format="file")` como dependencia explícita.
- Tests embebidos en `01_load_raw.R`; migrar a `tests/testthat/test-01_load_raw.R`.
- `_quarto.yml` minimalista; declarar `quarto-required: ">=1.5"`.

### T3 Prosa
- 21 secciones abriendo con "A partir de…" → metronome rhythm, suavizar.
- 17 instancias de "se procedió a" → muletilla, variar.
- 14 cierres con "coherente con/consistente con" → muletilla, variar.
- "Atlas" en título + Fig 4.10 vs decisión 2026-05-11.
- "aproximadamente 24 peptidoformas" → cuantificar exacto.
- Cifras de poder estadístico divergentes entre cap4.qmd y 410_discusion.qmd.

### T4 Figuras
- Fig 4.7 (stacked bars) usa paleta ggplot2 por defecto en lugar de `ptm_palette`.
- Fig 4.5 (volcano panel) monocromática; reemplazar por `14b_volcano_grid` que ya tiene paleta histona + Hedges g.
- Fig 4.8 (networks) tiene leyendas en inglés ("edges", "weight"); castellanizar.
- Inventario: 28 PNG + 28 PDF = 100 % cobertura dual. Sistema Visual Pelamovic respetado en 11/12 figuras principales.

### T5 Coherencia cap. 3 ↔ 4
- Cap. 4 §4.1.2 imputa al cap. 3 un filtro 34→30 que cap. 3 no contiene.
- H3K79 cuantificado en cap. 4 §4.7 con 4 peptidoformas (EIAQDFKTDLR), sin soporte metodológico en cap. 3.
- H3.1/H3.3 (H3_27_40 vs H33_27_40) sin contrato definido en cap. 3.
- Cap. 3 en inglés vs cap. 4 en castellano: política de bilingüismo o unificar.
- Cero referencias cruzadas formales "§3.X" en cap. 4.
- `EpiProfile-PLANTS` (cap. 4) vs `EpiProfile_PLANTS` (cap. 3): unificar grafía.

### T6 Literatura
- Discrepancia cuantitativa grave: 70 / 33 / 27 entradas según fuente.
- Cero autocitas del grupo (Pelayo, Valledor, Fraga).
- Franek 2023 vs Lochmanová 2024 MCP sobre PXD046034: aclarar si comparten dataset o son depósitos distintos.
- DOI sospechoso en Ryzhaya 2026 (`erag100`, patrón JXB es `eraXXX`).
- Pearson 1897, Tukey 1949, Sandve 2013 en bib pero sin citar.

## Plan de acción priorizado para v3.0.1 → v3.1.0

### Sprint inmediato (bloqueantes, antes de defensa)
1. **Reconciliar las 4 BH-FDR<0.05** (BLOQ-1): rerun stats con Rscript -e "targets::tar_invalidate(c('stats_pairwise','stats_hedges_ci')); targets::tar_make()" y publicar la verdad única en cap4.qmd + 411_resumen.qmd + capitulo4.qmd.
2. **Commit v3.0.0** + actualizar CITATION.cff + crear repo público + tag firmado (BLOQ-2).
3. **Editar título cap. 4** "Atlas ontogénico" → "Panel descriptivo composicional"; editar Fig 4.10 (BLOQ-4).
4. **Fig 4.7 con `ptm_palette`** (T4 hallazgo crítico 2).
5. **Inicializar git** en `D:/AT_virgen/histone_long_table/` + versionar `build_long_table.py` (BLOQ-5).

### Sprint medio (sustantivos, semana siguiente)
6. **Consolidar bibliografía** en un único .bib con ≥65 entradas reales (BLOQ-6).
7. **Reescribir cap. 3 §2.1.2** con lote 2025017 + n por estadio + DAS + variantes H2A (BLOQ-7).
8. **Bootstrap BCa** en 13c (T1).
9. **Migrar tests** a `tests/testthat/` (T2).
10. **Documentar invariancia de figuras** en `docs/decisions.md` (BLOQ-3).

### Sprint final (menores, antes del envío)
11. Suavizar metronome rhythm de prosa (T3).
12. Castellanizar leyendas figuras (T4).
13. Reportar BER en PLS-DA (T1).
14. Insertar referencias cruzadas formales §3.X (T5).
15. Verificar DOI Ryzhaya y limpiar bib (T6).
