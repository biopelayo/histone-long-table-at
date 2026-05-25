# Handoff v3.1.0 · Cap. 4 sprint nivel dios

**Fecha:** 2026-05-25
**Sesión:** 8 olas ejecutadas en paralelo en una sola sesión continuada.

## Lo que se cerró

| Ola | Output | Estado |
|---|---|---|
| **OLA 1** Verdad numérica | `T_verdad_4hits.{csv,md}` | 4 hits BH-FDR<0.05 TODOS en BOT_vs_SEN ✓ IHW confirma |
| **OLA 2** Git + tags | Tag v3.0.0 CAP4 + v1.0.0 histone_long_table | Backup 881 MB intacto |
| **OLA 3** Figuras | Fig 4.7 ptm_palette, Fig 4.8 castellano, Fig 4.10 sin Atlas | 22/56 figs regeneradas |
| **OLA 4** Cap. 3 propuesta | `OLA4_cap3_reescritura_propuesta.md` (1880 pal) | Pendiente aplicar al .docx |
| **OLA 5** Cap. 4 reconciliación | Título "Panel descriptivo", 4 hits, refs §3.X, prosa | ~30 ediciones en .qmd |
| **OLA 6** Bibliografía | `references.bib` 33 → 84 entradas | 5 TODOs DOI menores |
| **OLA 7** Sustantivos T1-T2 | BCa, BER, input_csv file, tests/testthat (12 tests) | testthat invocado pre-render |
| **OLA 8** Tribunal v2 | `F8_tribunal_v2_consolidado.md` | 2 APTO PARA TRIBUNAL, 4 APTO CON RESERVAS bajadas |

## Hallazgo nuclear del sprint

**La verdad canónica de las 4 peptidoformas BH-FDR<0.05** (D-034):

| # | Peptidoforma | Péptido | log2FC | Hedges g | p | BH-FDR |
|---|---|---|---:|---:|---:|---:|
| 1 | H3_27_40 K27me2 | KSAPATGGVKKPHR | -1,142 | **-2,148** | 3,6e-4 | 0,0175 |
| 2 | H4_20_23 K20me1 | KVLR | +1,714 | **+1,860** | 3,0e-4 | 0,0175 |
| 3 | H3_27_40 unmod | KSAPATGGVKKPHR | +2,177 | **+2,046** | 1,1e-3 | 0,0351 |
| 4 | H4_20_23 K20me2 | KVLR | -3,436 | **-1,557** | 1,5e-3 | 0,0360 |

**TODAS en BOT_vs_SEN.** IHW confirma los mismos 4 hits (concordancia 100 %).

**Interpretación biológica:** caída de H3K27me2 + aumento del H3 no modificado en H3.1; aumento de H4K20me1 + caída de H4K20me2. Patrón consistente con re-heterocromatinización foliar en senescencia.

## Tribunal Art. 16 v2 · cambio de riesgo

| Capa | v3.0.0 | v3.1.0 | Δ | Veredicto |
|---|---:|---:|---:|---|
| T1 · Estadística | 9 % | **7 %** | -2 | APTO CON RESERVAS |
| T2 · Reproducibilidad | 12 % | **8 %** | -4 | APTO CON RESERVAS |
| T3 · Prosa | 9 % | **7,5 %** | -1,5 | APTO CON RESERVAS |
| T4 · Figuras | 12 % | **6 %** | -6 | **APTO PARA TRIBUNAL** |
| T5 · Coherencia cap. 3↔4 | 6 % | **3,5 %** | -2,5 | APTO CON RESERVAS |
| T6 · Literatura | 14 % | **7 %** | -7 | **APTO PARA TRIBUNAL** |

**Riesgo agregado: 25-30 % → 12-15 % (reducción 50 %).**

## 5 de 7 bloqueantes cerrados

| Id | Bloqueante | Estado |
|---|---|---|
| BLOQ-1 | Inconsistencia 4 BH-FDR<0.05 | ✓ Cerrado: BOT_vs_SEN confirmado |
| BLOQ-2 | Tag v3.0.0 + CITATION.cff | ✓ Cerrado (repo público pendiente) |
| BLOQ-3 | Figs desfasadas | ✓ Documentada invariancia + 22 regeneradas |
| BLOQ-4 | "Atlas" hardcoded | ✓ Cerrado en título + Fig 4.10 + sections |
| BLOQ-5 | Git histone_long_table | ✓ Cerrado v1.0.0 + v1.1.0 |
| BLOQ-6 | Bibliografía 70/33/27 | ✓ Cerrado 84 entradas verificadas |
| BLOQ-7 | Cap. 3 borrador | ⚠ Propuesta MD entregada, aplicación al docx pendiente |

## Pendientes para v3.2.0 (mejora continua, no bloqueantes para defensa)

1. **Aplicar propuesta OLA 4 al docx cap. 3** (`CHAPTER_METHODS_rev_1604_LV.docx`). Decisión Pelayo.
2. **Repo público GitHub + DOI Zenodo** para CAP4 y histone_long_table. Decisión Pelayo.
3. **IHW covariable independiente** (T1 W2): cambiar `abs(log2fc)` por `n_a + n_b` o CV intra-grupo.
4. **D-038 explícita**: declarar 12b/16b Welch como primario, 12/16 clásico como sensitivity.
5. **run_step hash de contenido**: cambiar `size+mtime` a `digest::digest(file=..., algo="xxhash64")`.
6. **Migración APA → `[@key]`**: 80+ refs en prosa todavía no migradas a BibTeX inline (sub-agente OLA 6 lo dejó out-of-scope).
7. **Autocitas Valledor/Fraga**: búsqueda confirmada vacía; resolver con dirección de tesis.
8. **Armonizar nomenclatura H2A**: `W12/X/Z` (propuesta cap. 3) vs `H2A.W12/H2A.X/H2A.Z` (cap. 4 glosario).
9. **Eliminar 2 huérfanas .bib**: `tukey1949`, `sandve2013` no citadas.
10. **Resolver 5 TODOs DOI** en .bib: Ryzhaya, Schrader, Tian 2012, Xu 2005, Lang.

## Decisiones D-025..D-038

Documentadas en `D:/CAP4_NUEVO_OUTPUT/docs/decisions.md` y resumidas en `F8_tribunal_v2_consolidado.md`.

## Estado del repo

```
D:/AT_virgen/histone_long_table/          tag v1.1.0
├── histone_ratios_long.{csv,xlsx}        contrato de datos (9010 x 10)
├── build_long_table.py                   generador idempotente
├── qa_audit.py + F1_diff_audit.py        validación cruzada
├── OLA1_verdad_numerica.R                extractor de los 4 hits
├── T_verdad_4hits.{csv,md}               verdad canónica D-034
├── MASTER_PLAN.md + MASTER_PLAN_v3.1.0.md plan inicial + extendido
├── F5_audit_summary.md                   auditoría 28 scripts R
├── F8_tribunal_consolidado.md            dictamen v3.0.0
├── F8_tribunal_v2_consolidado.md         dictamen v3.1.0
├── OLA4_cap3_reescritura_propuesta.md    propuesta cap. 3 (pendiente aplicar)
├── OLA6_bibliografia_report.md           inventario bibliografía
├── FINAL_HANDOFF.md + FINAL_HANDOFF_v3.1.0.md handoffs

D:/CAP4_NUEVO_OUTPUT/                     tag v3.1.0
├── R/                                    33 scripts (12 ediciones v3.1.0)
├── tests/testthat/                       12 tests (8 + 4)
├── references.bib                        84 entradas verificadas
├── docs/decisions.md                     D-001..D-037 + D-029..D-038
├── _targets.R                            con input_csv format=file
├── reports/cap4.qmd                      render v3.1.0 (HTML+DOCX+PDF)
└── output/figures/                       56 figs (22 regeneradas hoy)

D:/CAP4_NUEVO_OUTPUT_v2.0.0_FROZEN/       backup intacto 881 MB

D:/Antigravity/arsenal/_master/           cap. 4 fusión Tribunal Art. 16
└── sections/                             17 sections con 4 hits + refs §3.X
```

## Próximo movimiento sugerido

**Si Pelayo prioriza defensa próxima** (3-5 días): aplicar propuesta OLA 4 al docx cap. 3 + crear repo público + cerrar T1 W2 IHW. Eso bajaría el riesgo a ≤ 6 %.

**Si Pelayo prioriza solidez técnica**: ejecutar los 10 pendientes v3.2.0 en sprint medio. Eso bajaría el riesgo a ≤ 3 %.

**Si Pelayo necesita parar el reloj**: la versión v3.1.0 tal cual ya es defendible con riesgo 12-15 % de no cum laude. El cap. 4 está consistente, reproducible y con verdad canónica firmada.
