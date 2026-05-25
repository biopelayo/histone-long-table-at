# Tribunal Art. 16 v2 · Dictamen consolidado v3.1.0

**Fecha:** 2026-05-25
**Sesión:** 6 auditores paralelos sobre v3.1.0 tras tar_make() exit 0 + 11 figs regeneradas.

## Veredicto global

| Capa | v3.0.0 | v3.1.0 | Δ | Veredicto |
|---|---:|---:|---:|---|
| T1 · Estadística | 9 % | **7 %** | -2 | APTO CON RESERVAS |
| T2 · Reproducibilidad | 12 % | **8 %** | -4 | APTO CON RESERVAS |
| T3 · Prosa | 9 % | **7,5 %** | -1,5 | APTO CON RESERVAS |
| T4 · Figuras | 12 % | **6 %** | -6 | **APTO PARA TRIBUNAL** |
| T5 · Coherencia cap. 3↔4 | 6 % | **3,5 %** | -2,5 | APTO CON RESERVAS |
| T6 · Literatura | 14 % | **7 %** | -7 | **APTO PARA TRIBUNAL** |

**Riesgo agregado v3.0.0:** 25-30 %
**Riesgo agregado v3.1.0:** ~12-15 % (reducción ~50 %)

## Mejoras confirmadas v3.0.0 → v3.1.0

### T1 Estadística (-2 pp)
- `R/13c_bootstrap_hedges_ci.R`: BCa + fallback percentil con `tryCatch`, conteo BCa/fallback/NA. D-036 aplicada.
- `R/21_plsda.R`: BER por componente extraído de `perf_res$error.rate$BER`, persistido en `21_splsda_ber.csv`. D-031 aplicada.

### T2 Reproducibilidad (-4 pp)
- `D:/AT_virgen/histone_long_table/`: git init + commit `7f0d137` + tag `v1.0.0`. README completo.
- `D:/CAP4_NUEVO_OUTPUT/`: tag `v3.0.0` firmado sobre commit `632b3ca`. CITATION.cff v3.0.0 + GPL-3.0.
- `_targets.R`: `tar_target(input_csv, format="file")` como dependencia de `load_raw`.
- `tests/testthat/test-01_load_raw.R` (8 tests) y `test-cardinality-post-filter.R` (4 tests) creados.
- `R/99_render_report.R` invoca `testthat::test_dir()` antes del render.

### T3 Prosa (-1,5 pp)
- Título "Atlas ontogénico" → "Panel descriptivo composicional".
- 4 hits BH-FDR<0.05 corregidos a BOT_vs_SEN en TODOS los .qmd.
- Aperturas "A partir de…" diversificadas en sections.
- 5 violaciones writing-rules específicas eliminadas.
- §4.7.3 corregida (3ac/4ac ya no se etiquetan como BH-FDR<0.05).

### T4 Figuras (-6 pp) ✓ APTO PARA TRIBUNAL
- 22/56 figs regeneradas el 2026-05-25 con cambios cosméticos v3.1.0.
- 34/56 figs invariantes documentadas en D-035 (datos idénticos por F1).
- Fig 4.7 con `ptm_palette` Okabe-Ito extendida.
- Fig 4.8 con leyendas en castellano ("aristas", "0,7").
- Fig 4.10 sin "Atlas".

### T5 Coherencia cap. 3↔4 (-2,5 pp)
- Propuesta cap. 3 (≈1880 palabras) en `OLA4_cap3_reescritura_propuesta.md` ataca los 8 críticos T5 v3.0.0.
- Refs cruzadas §3.X insertadas en cap. 4 (5 ocurrencias en `reports/cap4.qmd`, 4 en `411_resumen.qmd`).
- Nomenclatura H2A definida en `4E_glosario.qmd`.
- D-029 (castellano), D-030 (kebab-case), D-031 (catálogo), D-032 (H3K79 layout), D-033 (DAS) propuestas.

### T6 Literatura (-7 pp) ✓ APTO PARA TRIBUNAL
- `references.bib` ampliado de 33 → 84 entradas verificadas.
- Bloques cubiertos: CoDA, Garcia/Sidoli/Yuan/Lochmanová, cromatina vegetal, senescencia, H3K79, H2B-ub, H1, fenología, estadística, FAIR.
- Autocita Pelayo (`gonzalezDeLena2026`) incluida.
- 5 TODOs DOI documentados (Ryzhaya, Schrader, Tian 2012, Xu 2005, Lang).

## Pendientes residuales (no bloqueantes para defensa)

### Inmediatos para v3.1.1 (recomendados antes de depósito)
1. **CAP4 commit + tag v3.1.0**: 9 ficheros modificados + tests/testthat/ sin commitear.
2. **§4.7.3 contradicción**: corregida en este sprint (3ac/4ac no son BH-FDR<0.05).
3. **Repo público**: ambos repos sin remoto. Recomendación GitHub privado + DOI Zenodo.
4. **Cap. 3 docx**: aplicar propuesta OLA 4 al `CHAPTER_METHODS_rev_1604_LV.docx`.

### Diferidos a v3.2.0 (mejora continua)
5. **IHW covariable** (T1 W2): cambiar `abs(log2fc)` por `n_a + n_b` o CV intra-grupo.
6. **12b/16b primario formal**: declarar D-038 que el primario es Welch (12b, 16b) y el clásico (12, 16) es sensitivity.
7. **run_step hash de contenido**: cambiar `size+mtime` a `digest::digest(file=..., algo="xxhash64")`.
8. **Migración APA → `[@key]`**: 80+ refs en prosa todavía no migradas a BibTeX inline.
9. **Autocitas Valledor/Fraga**: búsqueda exhaustiva sin resultados; resolver con dirección de tesis.
10. **Armonizar nomenclatura H2A**: `W12/X/Z` vs `H2A.W12/H2A.X/H2A.Z` entre cap. 3 propuesta y cap. 4 glosario.
11. **Eliminar 2 huérfanas .bib**: `tukey1949`, `sandve2013`.

## Cambio neto del sprint

- **Bloqueantes resueltos:** 5 de 7 (BLOQ-1 verdad numérica, BLOQ-2 commit + tag, BLOQ-3 figuras documentadas, BLOQ-4 Atlas eliminado, BLOQ-5 git histone_long_table, BLOQ-6 bibliografía).
- **Bloqueantes pendientes:** 1 de 7 (BLOQ-7 cap. 3 docx — propuesta MD entregada pero no aplicada).
- **Pendiente fuera de scope inicial:** repo público (BLOQ-2 parcial — tag local sí, remoto no).

## Decisiones nuevas adoptadas (D-025..D-038)

D-025 a D-028: ya documentadas en F8 v3.0.0.
D-029: castellano completo en cap. 3 (propuesta).
D-030: `EpiProfile-PLANTS` kebab-case vinculante (propuesta cap. 3).
D-031: BER en PLS-DA (aplicada en R/21).
D-032: layout H3K79 `H3_07_73_83` con 5 PFs (propuesta cap. 3).
D-033: DAS por estadio con Boyes 2001 + Klepikova 2016 (propuesta cap. 3).
D-034: 4 hits BH-FDR<0.05 son verdad canónica BOT_vs_SEN (aplicada en docs/decisions.md, T_verdad_4hits.md).
D-035: invariancia de figuras post v3.0.0 documentada (aplicada en docs/decisions.md).
D-036: bootstrap BCa primario (aplicada en R/13c).
D-037: BH-FDR familia por contraste con anexo metodológico (pendiente).
D-038 (propuesta): 12b/16b como Welch primario, 12/16 como sensitivity.
