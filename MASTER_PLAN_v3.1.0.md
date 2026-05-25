# Master Plan v3.1.0 — Cierre nivel dios de los 7 bloqueantes + sustantivos

**Fecha:** 2026-05-25
**Estado v3.0.0:** APTO CON RESERVAS, riesgo agregado 25-30 % de no cum laude.
**Objetivo v3.1.0:** APTO PARA TRIBUNAL, riesgo ≤ 5 %.

---

## Orden lógico por dependencias (no por urgencia)

Cada ola desbloquea las siguientes. No saltar.

```
OLA 1  Verdad numérica  (BLOQ-1)
   │
   ▼
OLA 2  Infraestructura git  (BLOQ-2 + BLOQ-5)   ← paraleliza con OLA 3
   │
   ▼
OLA 3  Figuras y título  (BLOQ-3 + BLOQ-4)
   │
   ▼
OLA 4  Cap. 3 reconstrucción  (BLOQ-7)
   │
   ▼
OLA 5  Cap. 4 reconciliación  (T3 + T5 + cifras OLA 1)
   │
   ▼
OLA 6  Bibliografía consolidada  (BLOQ-6)
   │
   ▼
OLA 7  Hallazgos sustantivos T1-T2  (BCa, tests, run_step)
   │
   ▼
OLA 8  Render final + segundo Tribunal Art. 16
```

---

## OLA 1 · Verdad numérica (~30 min) — BLOQ-1

**Por qué primero:** toda la prosa downstream cita cifras y peptidoformas concretas. Sin la verdad canónica, cualquier reescritura es humo.

### Tareas

| Id | Acción | Output |
|---|---|---|
| 1A | `tar_invalidate(c("stats_pairwise","stats_hedges_ci","stats_welch_anova","stats_permutation","ihw_alternative"))` + `tar_make()` | rds frescos |
| 1B | Script R que lea `13_stats_pairwise.rds` y `13c_bootstrap_hedges_ci.rds`, filtre `fdr_bh<0.05`, ordene por |Hedges g| | `T_verdad_4hits.csv` |
| 1C | Cross-check con `13b_stats_permutation` y `23_ihw_alternative` para los mismos 4 hits | columna `concordancia` |
| 1D | Tabla canónica con: contraste, peptidoforma, péptido, p-valor Welch, fdr_bh, Hedges g, IC95% percentil, IC95% BCa (si disponible) | `T_verdad_4hits.md` |

### Criterio de cierre
- Las 4 peptidoformas BH-FDR<0.05 quedan listadas con contraste exacto (BOT-SEN o FLOR-SEN o ambos).
- Si las cifras nuevas difieren del v2.0.0, documentar por qué (no deberían, por F1).

### Riesgo gestionado
- Si surgen más de 4 hits: actualizar todo el discurso del cap. 4 a la cifra real.
- Si surgen menos de 4: idem.

---

## OLA 2 · Infraestructura git (~1-2 h) — BLOQ-2 + BLOQ-5

**Por qué después de OLA 1:** los commits deben incluir la verdad numérica reconciliada.

### Tareas en paralelo

**Track A · `D:/AT_virgen/histone_long_table/` (BLOQ-5)**
| Id | Acción |
|---|---|
| 2A1 | `git init`, `.gitignore` (excluir `__pycache__`, `*.pyc`, `.ipynb_checkpoints`) |
| 2A2 | Versionar `build_long_table.py`: añadir `__version__ = "1.0.0"`, embeber en CSV (columna `meta_version`) y header de XLSX |
| 2A3 | Embeber SHA256 del TXT crudo origen en `QA_report.txt` |
| 2A4 | Commit inicial + tag `v1.0.0` |

**Track B · `D:/CAP4_NUEVO_OUTPUT/` (BLOQ-2)**
| Id | Acción |
|---|---|
| 2B1 | Actualizar `CITATION.cff`: version `3.0.0`, date_released `2026-05-25` |
| 2B2 | Añadir `.gitignore` extendido: `*.log`, `tmp_*.R`, `_targets/`, `_freeze/`, `tar_make_v*.log` |
| 2B3 | Mover `R/*.bak` a `archive/` |
| 2B4 | Commit selectivo de los 12 modificados + 9 untracked con mensaje detallado |
| 2B5 | Tag firmado `v3.0.0` con changelog |
| 2B6 | (opcional, requiere acción Pelayo) Crear repo GitHub público + push + DOI Zenodo |

### Criterio de cierre
- `git status` limpio en ambos repos.
- Tag `v3.0.0` en `D:/CAP4_NUEVO_OUTPUT/` y `v1.0.0` en `D:/AT_virgen/histone_long_table/`.
- (Si opcional) repo público accesible.

---

## OLA 3 · Figuras y título (~1 h) — BLOQ-3 + BLOQ-4

**Por qué después de OLA 1+2:** las figuras nuevas deben citar las 4 peptidoformas reales y quedar versionadas.

### Tareas

| Id | Acción | Fichero |
|---|---|---|
| 3A | Reemplazar "Atlas" por "Panel descriptivo" | `R/25_fig_workflow_cap4.R` líneas 33 y 41 |
| 3B | Añadir `scale_fill_manual(values = ptm_palette)` con derivación de PTM-class por regex | `R/17_stacked_barplots.R` línea 49 |
| 3C | Castellanizar leyendas networks: "edges" → "aristas", "abs(weight)" → "\|peso\|" | `R/18_correlation_networks.R` |
| 3D | Sustituir Fig 4.5 en QMD por `14b_volcano_grid` (mejor aesthetic) | `reports/cap4.qmd` |
| 3E | `tar_invalidate(c("stacked_bars","fig_workflow_cap4"))` + `tar_make()` | regenera Fig 4.7 + 4.10 |
| 3F | Crear `docs/decisions.md` documentando invariancia de Fig 4.0-4.4, 4.6, 4.8, 4.9 (mismas porque F1 demostró igualdad numérica) | nueva |
| 3G | Verificar paridad PNG+PDF en `figs/` post-rerun | bash check |

### Criterio de cierre
- Fig 4.7 con colores `#4477AA` (me1), `#228833` (me2), `#AA3377` (me3), `#CCBB44` (ac).
- Fig 4.10 sin la palabra "Atlas".
- `docs/decisions.md` explica la invariancia documentadamente.

---

## OLA 4 · Cap. 3 reconstrucción (~3-5 h, lo más largo) — BLOQ-7

**Por qué después de OLA 3:** el cap. 3 debe convergir con la nomenclatura y cifras que usa cap. 4.

### Tareas secuenciales

| Id | Acción | Output |
|---|---|---|
| 4A | Leer `D:/AT_virgen/CHAPTER_METHODS_rev_1604_LV.docx` completo | inventario de problemas |
| 4B | Eliminar notas embebidas del codirector LV; completar tablas con numeración rota (`Table 245` → numeración real) | borrador limpio |
| 4C | Reescribir §2.1.2 con lote `2025017`, n por estadio (5/11/8/9 inicial, 5/11/8/9 post-QC), DAS por estadio (YNG 21-25, BOT 28-32, FLOR 35-42, SEN 45-55) + cita Boyes 2001 + Klepikova 2016 | §2.1.2 v2 |
| 4D | Añadir §3.B.X con catálogos por familia histónica: H1=6 PF, H2A=22 PF (incluye variantes W6, W12, X, Xa, Z), H2B=13 PF, H3=37 PF, H3.3=10 PF, H4=9 PF | §3.B.X nueva |
| 4E | Glosario de nomenclatura H2A: definir `H2A_can`, `H2A_W6`, `H2A_W12`, `H2A_X`, `H2A_Xa`, `H2A_Z` con secuencias canónicas y referencias | tabla glosario |
| 4F | Resolver H3K79: declarar layout `H3_73_83 EIAQDFKTDLR` con K79me1/me2/me3/ac como parte estable del bundle EpiProfile-PLANTS, citar Wood-Tellier-Murphy 2018 + Steger 2008 | §3.X H3K79 |
| 4G | Unificar grafía `EpiProfile-PLANTS` (kebab-case) en cap. 3 | search-replace |
| 4H | Decidir política bilingüismo: cap. 3 a castellano completo (recomendado) o mantener inglés con justificación | decisión D-029 |
| 4I | Eliminar de cap. 3 menciones a *Marchantia* y *Chlamydomonas* si no se usan en bundle | poda |

### Criterio de cierre
- Cap. 3 sin notas embebidas, sin tablas rotas, sin secciones placeholder.
- Lote 2025017 documentado con detalle MIAPE.
- Nomenclatura H2A completa.
- H3K79 con soporte metodológico explícito.

---

## OLA 5 · Cap. 4 reconciliación (~2 h) — T3 + T5 + OLA 1

**Por qué después de OLA 4:** las referencias cruzadas §3.X requieren que cap. 3 esté estable.

### Tareas

| Id | Acción | Fichero |
|---|---|---|
| 5A | Cambiar título "Atlas ontogénico" → "Panel descriptivo composicional" | `arsenal/_master/capitulo4.qmd` línea 1, `reports/cap4.qmd` |
| 5B | Insertar las 4 peptidoformas reconciliadas de OLA 1 con contraste único | `reports/cap4.qmd` §4.9.1, `411_resumen.qmd` línea 11, `capitulo4.qmd` resumen |
| 5C | Insertar referencias cruzadas formales §3.X (§3.2.1, §3.B.X, §3.X H3K79) | múltiples sections |
| 5D | Suavizar 21 aperturas "A partir de…" → variar (sustituir por conector + verbo activo) | 21 sections |
| 5E | Variar 17 "se procedió a" → verbos activos directos | múltiples |
| 5F | Variar 14 "coherente con / consistente con" → "concuerda con / refuerza / replica" | múltiples |
| 5G | Cuantificar exacto "aproximadamente 24 peptidoformas" | línea 261 cap4.qmd |
| 5H | Reconciliar cifras de poder estadístico entre cap4.qmd §4.6.5 y 410_discusion.qmd §4.10.1 (un único valor Monte Carlo) | dos secciones |
| 5I | Anexo metodológico justificando BH familia por contraste con cita BH 1995 §3 | 4A_sensibilidad.qmd |
| 5J | Eliminar 5 violaciones específicas writing-rules de T3 (cap4:295, 69, 359; 410:7; 411:7) | 4 sections |
| 5K | Promover §16b Welch a primario en single PTMs; §16 como sensibilidad | §4.7.X reformulación |

### Criterio de cierre
- Resumen y discusión coherentes en cifras y peptidoformas.
- Cero "Atlas" residual.
- Cero metronome rhythm detectable.

---

## OLA 6 · Bibliografía consolidada (~2 h) — BLOQ-6

**Por qué después de OLA 5:** las citas requieren que cap. 3 y cap. 4 estén estables para inventariar todas.

### Tareas

| Id | Acción |
|---|---|
| 6A | Inventario de todas las citas en cap. 3 + cap. 4 (master + sections + reports). Grep `@\w+` + búsqueda manual de citas APA en prosa |
| 6B | Comparar inventario vs `references.bib` actual (33 entradas). Listar faltantes |
| 6C | Añadir refs críticas faltantes al .bib: Lochmanová 2019, 2024 ×2 (MCP, Plants), Bourbousse 2012, Sidoli 2014, Sidoli & Garcia 2017, Schräder 2018, Yuan 2014/2018, Hedges 1981, Cohen 1988, Gloor 2017, Lovell 2015, Wilkinson 2016, Yelagandula 2014, Talbert & Henikoff 2017, Sridhar 2007, Cao 2008, Steger 2008, Wollmann 2012, Jacob 2009/2014, Schubert 2006, Margueron 2011, Narita 2003, Adams 2007, Beck 2012, Boyes 2001, Klepikova 2016, Roudier 2011, Borg 2020, Buchanan-Wollaston 2005 |
| 6D | Añadir 2-3 autocitas Pelayo/Valledor/Fraga (epi-proteómica vegetal grupo) |
| 6E | Verificar DOI Ryzhaya 2026 (sospechoso `erag100`) |
| 6F | Eliminar Pearson 1897, Tukey 1949, Sandve 2013 si no se citan |
| 6G | Aclarar nominalmente en §4.10.4 si Franek 2023 y Lochmanová 2024 MCP comparten PXD046034 |
| 6H | Migrar todas las citas APA-en-prosa a `[@key]` BibTeX con `cite-method: citeproc` |
| 6I | Verificar `references.bib` >= 65 entradas; eliminar las dos bibliografías paralelas (reports/master) |

### Criterio de cierre
- Un único `references.bib` con ≥65 entradas verificadas (DOI, autores, año).
- Cero referencias huérfanas (todas citadas en cuerpo).
- Cero referencias citadas en cuerpo sin entrada .bib.

---

## OLA 7 · Hallazgos sustantivos T1-T2 (~2 h)

**Por qué después de OLA 6:** son mejoras de robustez técnica que no afectan a cifras ni prosa.

### Tareas T1 (estadística)

| Id | Acción | Fichero |
|---|---|---|
| 7A1 | Cambiar bootstrap percentil por BCa: `boot::boot.ci(..., type="bca")`. Si BCa falla para grupo n=5, fallback percentil con log warning. | `R/13c_bootstrap_hedges_ci.R` |
| 7A2 | Reportar BER (balanced error rate) en PLS-DA, no accuracy | `R/21_plsda.R` |
| 7A3 | Reportar df de Welch efectivo por contraste | `R/13_stats_pairwise.R` |
| 7A4 | Cambiar covariable IHW de `abs(log2fc)` a `n_a + n_b` o CV intra-grupo | `R/23_ihw_alternative.R` |

### Tareas T2 (reproducibilidad)

| Id | Acción | Fichero |
|---|---|---|
| 7B1 | Cambiar `run_step()` hash de rds a `digest::digest(file=..., algo="xxhash64")` | `_targets.R` |
| 7B2 | Añadir `tar_target(input_csv, paths$input_long_csv, format="file")` como dependencia explícita de `load_raw` | `_targets.R` |
| 7B3 | Crear `tests/testthat/test-01_load_raw.R` migrando los `expect_equal` embebidos | nueva |
| 7B4 | Crear `tests/testthat/test-cardinality.R` con n=34, 5+11+9+9, 265 PF | nueva |
| 7B5 | Invocar `testthat::test_dir("tests/testthat")` en `R/99_render_report.R` | edit |
| 7B6 | Fijar Quarto en `_quarto.yml`: `quarto-required: ">=1.5"`, declarar `engine: knitr` | edit |
| 7B7 | Documentar `renv::status()` en README del repo | nueva sección |

### Criterio de cierre
- `tar_make()` exit 0 con todos los tests pasando.
- `R CMD check` sin warnings ni notes.

---

## OLA 8 · Render final + segundo Tribunal Art. 16 (~1 h)

**Por qué último:** validación independiente sobre el cuerpo completo v3.1.0.

### Tareas

| Id | Acción |
|---|---|
| 8A | `tar_invalidate(everything())` + `tar_make()` desde cero. Verificar exit 0 |
| 8B | Verificar 3 renders: HTML + DOCX + PDF |
| 8C | Lanzar 6 sub-agentes paralelos Tribunal Art. 16 v2: T1 a T6 |
| 8D | Consolidar dictamen v2. Si algún veredicto sigue "APTO CON RESERVAS", crear plan v3.2.0 |
| 8E | Si todos APTO PARA TRIBUNAL: tag `v3.1.0` + handoff final + memoria |
| 8F | Update `MEMORY.md` con el cierre |

### Criterio de cierre
- 6× APTO PARA TRIBUNAL.
- Riesgo agregado ≤ 5 %.
- Tag firmado `v3.1.0`.

---

## Estimación de tiempo total

| Ola | Tiempo | Acumulado |
|---|---:|---:|
| 1 | 0.5 h | 0.5 h |
| 2 | 1.5 h | 2.0 h |
| 3 | 1.0 h | 3.0 h |
| 4 | 4.0 h | 7.0 h |
| 5 | 2.0 h | 9.0 h |
| 6 | 2.0 h | 11.0 h |
| 7 | 2.0 h | 13.0 h |
| 8 | 1.0 h | 14.0 h |

**Total ≈ 14 horas de trabajo efectivo.** Repartibles en 2-3 sesiones largas o 4-5 sesiones cortas.

---

## Decisiones nuevas previstas (D-029..D-033)

- **D-029** Política idiomática: tesis completa en castellano de España, cap. 3 reescrito.
- **D-030** Bootstrap BCa primario para Hedges g, percentil como fallback documentado.
- **D-031** PLS-DA reporta BER, no accuracy.
- **D-032** BH-FDR familia = contraste (justificado en §4.A nuevo anexo).
- **D-033** Repositorio público con DOI Zenodo como sede canónica.

---

## Próximo movimiento inmediato

Arranco **OLA 1A** ahora: `tar_invalidate` + `tar_make` para regenerar stats con la nueva tabla y obtener las 4 peptidoformas reales BH-FDR<0.05.
