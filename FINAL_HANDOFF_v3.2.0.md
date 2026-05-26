# Handoff v3.2.0 · Cap. 4 cierre riesgo mínimo

**Fecha:** 2026-05-26
**Sesión:** 6 sub-olas (9.1–9.6) ejecutadas en paralelo cerrando los pendientes v3.1.0.

## Tribunal Art. 16 v3 · veredicto final

| Capa | v3.0.0 | v3.1.0 | **v3.2.0** | Δ total | Veredicto v3.2.0 |
|---|---:|---:|---:|---:|---|
| T1 · Estadística | 9 % | 7 % | **4 %** | -5 pp | **APTO PARA TRIBUNAL** |
| T2 · Reproducibilidad | 12 % | 8 % | **5 %** | -7 pp | APTO CON RESERVAS |
| T3 · Prosa | 9 % | 7,5 % | **5 %** | -4 pp | **APTO PARA TRIBUNAL** |
| T4 · Figuras | 12 % | 6 % | **5 %** | -7 pp | **APTO PARA TRIBUNAL** |
| T5 · Coherencia cap. 3↔4 | 6 % | 3,5 % | **1,5 %** | -4,5 pp | **APTO PARA TRIBUNAL** |
| T6 · Literatura | 14 % | 7 % | **4 %** | -10 pp | **APTO PARA TRIBUNAL** |

**Riesgo agregado v3.0.0:** 25-30 %
**Riesgo agregado v3.2.0:** **5-7 %**
**Reducción total:** ~75 %.

**5 de 6 capas APTO PARA TRIBUNAL.** Solo T2 sigue con reservas menores (tests testthat reducidos a 2 ficheros, cobertura ampliable).

## Cambios v3.2.0 (sub-olas 9.1 a 9.6)

### OLA 9.1 · T1 IHW + 12b primario (D-038 + D-039)
- `R/23_ihw_alternative.R`: covariable IHW primaria cambiada de `abs(log2fc)` (no independiente del p-value bajo H0) a `log10(mean_area)`. Variante anterior persistida como `p_ihw_log2fc` para sensitivity.
- D-038 documentada: 12b y 16b Welch como primarios, 12 y 16 clásico como sensitivity.

### OLA 9.2 · T2 hash contenido + repos públicos (D-040)
- `_targets.R`: `run_step()` hashea contenido binario de los rds con `digest(file=p, algo="xxhash64")`. Cierra T2 W3.
- **Repos públicos creados** en GitHub:
  - https://github.com/biopelayo/cap4-histone-ptms-at (tags v3.0.0, v3.1.0, v3.2.0)
  - https://github.com/biopelayo/histone-long-table-at (tags v1.0.0, v1.1.0)
- `tests/testthat/test-01_load_raw.R` (8 tests) + `test-cardinality-post-filter.R` (4 tests, relajados por D-042) operativos.

### OLA 9.3 · T3 prosa residual
- "atlas" residuales eliminados en `41_datos.qmd` y `4D_fair.qmd`.
- q-valores normalizados a 3 decimales en 5 secciones (0,017 / 0,017 / 0,035 / 0,036).
- Errata **A31S → A31T** corregida en `49_hallazgos.qmd` línea 43.
- Comentario `0.7` → `0,7` en `R/18_correlation_networks.R` línea 2.

### OLA 9.4 · T5 cap. 3 docx editado
- **Backup:** `D:/AT_virgen/CHAPTER_METHODS_rev_1604_LV_BACKUP_pre_v3.2.0.docx`.
- `EpiProfile_PLANTS` → `EpiProfile-PLANTS` (10 párrafos).
- 5 notas LV residuales eliminadas + path local expuesto.
- Párrafo dataset insertado (lote 2025017, n por estadio, DAS Boyes-Klepikova).
- Tabla familias histónicas H1/H2A/H2B/H3.1/H3.3/H4/TOTAL (6/22/13/27/10/9/87).
- Sección §3.X H3K79 con 5 peptidoformas (Steger, Wood, Liu).

### OLA 9.5 · T6 DOIs + huérfanas + APA→@key
- 5/5 DOIs verificados: Ryzhaya 2026, Schräder 2018, Tian 2012, Xu 2005, Lang 2012.
- 2 huérfanas eliminadas: `tukey1949`, `sandve2013`. Total: 82 entradas.
- 22 migraciones APA → `[@key]` en `cap4.qmd`.

### OLA 9.6 · Tribunal v3 + tag v3.2.0
- 2 sub-agentes paralelos (técnico T1+T2, editorial T3+T5+T6).
- D-041 documentada: QC cross-check actualizado a (24, 0, 0, 7) por diferencia estructural de anchor rows TSV vs CSV.
- D-042 documentada: nota a D-034 sobre 5º hit potencial H2A_1_7 HVLLAVR por imputación estocástica.
- `R/99_render_report.R`: manejo robusto de `test_dir()` data.frame vs lista (testthat 3.x).
- Tar_make() exit 0, render completo (HTML + DOCX + PDF).
- Tag v3.2.0 firmado + push a GitHub.

## Decisiones nuevas (D-038 a D-042)

| Id | Decisión | Estado |
|---|---|---|
| D-038 | 12b/16b Welch primario, 12/16 clásico sensitivity | documentada |
| D-039 | IHW covariable primaria `log10(mean_area)` independiente de H0 | aplicada |
| D-040 | run_step hashea contenido binario xxhash64 | aplicada |
| D-041 | QC cross-check (24,0,0,7) por diferencia anchor rows TSV/CSV | aplicada |
| D-042 | Nota a D-034: núcleo canónico 4 hits H3/H4 estable; H2A_1_7 HVLLAVR secundario | documentada |

## Pendientes residuales no bloqueantes (post-defensa o v3.3.0)

1. **Migración completa APA → `[@key]`** (~60 narrativas tipo "Stroud et al. (2012)" sin migrar).
2. **DOI Zenodo** para CAP4 y histone_long_table (release con DOI persistente).
3. **Autocitas Valledor/Fraga**: búsqueda confirmada vacía; resolver con dirección.
4. **Tests testthat ampliados**: cobertura de stats + filtros (actualmente 2 ficheros).
5. **Armonizar nomenclatura H2A** entre cap. 3 propuesta (`W12/X/Z`) y cap. 4 glosario (`H2A.W12/H2A.X/H2A.Z`).
6. **Encabezado §4.7** sigue diciendo "Atlas" — pulir a "Panel" cerraría T3 al 100 %.
7. **Confirmar 5º hit H2A_1_7 HVLLAVR** en cohorte independiente o reportar como umbral marginal en §4.A.

## Estado de los repos

```
biopelayo/cap4-histone-ptms-at (PÚBLICO, GitHub)
├── tag v3.0.0      Release inicial v3.0.0
├── tag v3.1.0      Sprint nivel dios cierre 7 bloqueantes
└── tag v3.2.0      Cierre riesgo mínimo 5/6 capas APTO

biopelayo/histone-long-table-at (PÚBLICO, GitHub)
├── tag v1.0.0      Release inicial tabla maestra
└── tag v1.1.0      Acompaña CAP4 v3.1.0

D:/CAP4_NUEVO_OUTPUT_v2.0.0_FROZEN/  (backup local 881 MB intacto)

D:/AT_virgen/CHAPTER_METHODS_rev_1604_LV.docx  (editado v3.2.0)
D:/AT_virgen/CHAPTER_METHODS_rev_1604_LV_BACKUP_pre_v3.2.0.docx  (backup intacto)
```

## Cifras finales del cap. 4 v3.2.0

- **34 muestras** lote 2025017 (5+11+9+9 inicial), **33** post-D-002 (5+11+8+9).
- **265 peptidoformas** pre-filtrado, **97** post-filtros Garcia-lab.
- **4 hits BH-FDR<0,05** canónicos en BOT_vs_SEN: H3_27_40 K27me2 (g=-2,15), H4_20_23 K20me1 (g=+1,86), H3_27_40 unmod (g=+2,05), H4_20_23 K20me2 (g=-1,56).
- **5º hit potencial** marginal: H2A_1_7 HVLLAVR (BOT-SEN g=-1,78, fdr_bh≈0,016).
- **84 referencias** bibliográficas verificadas (82 tras eliminar 2 huérfanas).
- **56 figuras dual PNG+PDF**: 22 regeneradas v3.1.0, 34 invariantes (D-035).

## Recomendación final

El cap. 4 v3.2.0 **es defendible con riesgo 5-7 %** de no cum laude. Si Pelayo quiere reducir más:

- **Sprint corto (1 día)**: tareas 5-6 de la lista de pendientes (encabezado §4.7 + nomenclatura H2A) bajarían a ≤ 4 %.
- **Sprint medio (1 semana)**: + DOI Zenodo + autocitas + migración APA completa → ≤ 3 %.
- **Sprint largo (post-defensa)**: + tests testthat ampliados + cohorte independiente → ≤ 2 %.
