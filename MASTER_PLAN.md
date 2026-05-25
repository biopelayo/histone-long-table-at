# Master Plan v3.0.0 — Cap. 4 sobre tabla maestra refrescada

**Fecha:** 2026-05-24
**Autor:** Pelayo + asistencia Claude (Opus 4.7, 1M ctx)
**Estado:** propuesto, pendiente de validación por el usuario

---

## 0. Punto de partida

### 0.1 Lo que hay

- **Pipeline R/targets maduro** en `D:/CAP4_NUEVO_OUTPUT/` con 33 targets, capas Garcia-lab + CoDA + Welch + Hedges g + bootstrap CI + IHW + PLSDA + cluster validation. Estado: cap. 4 v2.0.0 ya renderizado.
- **Versión fusionada Tribunal Art. 16** en `D:/Antigravity/arsenal/_master/capitulo4.qmd` v1.0.0 (.html 2,2 MB + .docx 99 KB). Apto para tribunal con 33 muestras (5+11+8+9) y 97 peptidoformas filtradas.
- **Nueva tabla maestra** generada hoy en `D:/AT_virgen/histone_long_table/histone_ratios_long.{csv,xlsx}`: 9010 filas tidy = 265 peptidoformas × 34 muestras (5+11+9+9). Validada con 5 sanity checks vs raw (precisión < 1e-6).

### 0.2 Diagnóstico diferencial (el problema)

| Aspecto | Pipeline actual (v2.0.0) | Tabla nueva |
|---|---:|---:|
| Fichero origen | `D:/CAP4_NUEVO_INPUT/histone_ratios.txt` | `Downloads/histone_ratios_nucleosoma_completo_para completar.txt` |
| md5 | `11d5b71d...` | `0d242659...` |
| Columnas TSV | 105 | **107** |
| Muestras | 33 (post-filtrado) | 34 (pre-filtrado) |
| Peptidoformas | 97 (post-filtrado) | 265 (pre-filtrado) |
| Grupos | 5+11+8+9 | 5+11+9+9 |

**Implicaciones inmediatas:**

1. El `01_load_raw.R` aborta con el nuevo fichero (`stopifnot(ncols == 105)`).
2. Una muestra FLOR adicional → recalibrar diseño experimental.
3. 168 peptidoformas más → recalibrar todos los filtros (sensitivity, isobar resolution, abundance, RT-CV).
4. Los hashes de targets se invalidarán en cascada desde `load_raw` hasta `report` → re-ejecución completa del pipeline.

### 0.3 Objetivo

Cap. 4 v3.0.0 reproducible, con la tabla maestra refrescada como única fuente de verdad, manteniendo las 24 decisiones D-001 a D-024 del v2.0.0 y la revisión Tribunal Art. 16.

---

## 1. Principios rectores

- **Tabla maestra = contrato.** El XLSX/CSV en `D:/AT_virgen/histone_long_table/` es el único punto de entrada. El TSV crudo queda archivado como evidencia histórica, no como input vivo.
- **Versionado obligatorio.** Backup del v2.0.0 intacto antes de cualquier cambio.
- **Decisiones D-001 a D-024 son ley.** Cualquier cambio sustantivo necesita una D-025+ documentada.
- **Capa de control independiente (Constitución Pelamovic Art. 16).** Todo cambio sustantivo pasa por agente paralelo antes de quedar firme.
- **Revisión paso a paso con el usuario.** No hay run silencioso; cada script R se discute, valida y decide antes de avanzar.

---

## 2. Arquitectura objetivo

```
D:/AT_virgen/histone_long_table/         <-- nueva sede de la tabla maestra
├── histone_ratios_long.{csv,xlsx}       <-- contrato de datos (9010 x 10)
├── region_peptide_mapping.csv           <-- lookup canónico
├── build_long_table.py                  <-- generador idempotente
├── qa_audit.py                          <-- validación cruzada
└── MASTER_PLAN.md                       <-- este documento

D:/CAP4_NUEVO_OUTPUT/                    <-- pipeline R (modificado)
├── R/01_load_raw.R                      <-- REEMPLAZADO: carga CSV largo
├── R/02_design.R                        <-- AJUSTADO: nuevo design (34 muestras)
├── R/04_filter_samples.R                <-- REVISADO: decidir muestra del 81% ceros
├── R/06h_filter_nonzero_per_group.R     <-- VALIDADO: nuevos grupos
├── _targets.R                           <-- sin cambios estructurales
└── data/processed/*.rds                 <-- regenerados en cascada

D:/Antigravity/arsenal/_master/          <-- versión fusionada
└── capitulo4.qmd                        <-- actualizado con nuevos resultados
```

---

## 3. Fases del plan

### F1 · Diagnóstico diferencial detallado (sesión 1, ~1-2 h)

**Objetivo:** entender qué cambia entre v2.0.0 y los nuevos datos antes de tocar código.

**Entregables:**

1. Diff muestra a muestra: ¿qué muestra FLOR es nueva? ¿alguna del v2.0.0 desapareció o cambió?
2. Diff peptidoforma a peptidoforma: ¿qué 168 peptidoformas son nuevas? ¿alguna se renombró o desapareció? ¿alguna región nueva?
3. Diff valor a valor: para las peptidoformas comunes, ¿coinciden los valores? Si no, ¿en cuánto?
4. Decisión D-025: ¿el nuevo fichero reemplaza al anterior o se trata como una segunda batch?

**Script propuesto:** `D:/AT_virgen/histone_long_table/F1_diff_audit.py`

**Control independiente:** segundo pase con regla "diff sin asunciones" — listar todas las diferencias sin interpretar.

### F2 · Versionado y aislamiento (sesión 1, ~30 min)

**Objetivo:** preservar el v2.0.0 intacto y crear espacio limpio para v3.0.0.

**Acciones:**

1. Backup explícito: `cp -r D:/CAP4_NUEVO_OUTPUT D:/CAP4_NUEVO_OUTPUT_v2.0.0_FROZEN`
2. Tag git: `git tag v2.0.0-frozen` en `D:/CAP4_NUEVO_OUTPUT/`
3. Crear branch `v3.0.0-data-refresh` o copia de trabajo
4. Backup del cap. 4 fusionado: `cp capitulo4.qmd capitulo4_v1.0.0_frozen.qmd` en `_master/`

### F3 · Adaptación del cargador R/01 (sesión 2, ~1-2 h)

**Objetivo:** que el pipeline lea la tabla maestra en lugar del TSV crudo.

**Diseño:**

- Opción A (mínimo cambio): generalizar `01_load_raw.R` para que acepte 105 o 107 cols. Mantiene la lógica de detección de bloques.
- Opción B (recomendada): reemplazar `01_load_raw.R` por una carga directa del `histone_ratios_long.csv`. El parser Python ya hizo el trabajo sucio y está validado.

**Recomendación:** B. Razones:
- La tabla larga ya pasó QA cruzada (5 sanity checks OK)
- Incluye `region` como columna (el pipeline R no la tiene y la deriva implícitamente)
- Más simple: `read_csv()` y `pivot` a los 3 sub-tibbles que el pipeline espera
- Si mañana viene un nuevo fichero del MS, se actualiza `build_long_table.py` (Python) sin tocar R

**Implementación nuevo `01_load_raw.R`:**

```r
# Lee la tabla maestra y devuelve tres tibbles long-format
load_long <- function(path = paths$input_long_csv) {
  long <- readr::read_csv(path, show_col_types = FALSE)
  # Validar contrato
  required <- c("sample_index", "sample_name", "sample_code", "sample_group",
                "region", "peptide", "peptidoform",
                "ratio", "area", "retention_time")
  testthat::expect_setequal(names(long), required)
  list(
    ratio   = long |> select(peptide, peptidoform, sample = sample_name, ratio),
    area    = long |> select(peptide, peptidoform, sample = sample_name, area),
    rt      = long |> select(peptide, peptidoform, sample = sample_name, rt_min = retention_time),
    samples = long |> distinct(sample_name) |> pull(sample_name)
  )
}
```

**Control independiente:** test que verifica que `nrow(ratio) == 9010` y los 5 valores aleatorios del QA python coinciden.

### F4 · Ajuste del diseño experimental R/02 (sesión 2, ~30 min)

**Objetivo:** el `02_design.R` tiene que producir un diseño con 34 muestras y la distribución 5+11+9+9.

**Decisión D-026 propuesta:** ¿se mantienen las 4 categorías {YNG, BOT, FLOR, SEN}? ¿se hace algún reagrupamiento? Mi recomendación: mantener D-001 (4 grupos canónicos).

### F5 · Revisión paso a paso del pipeline (sesiones 3-7, multi-sesión)

**Esto es el corazón del plan.** Iremos juntos por cada script R, en este orden:

| Script | Foco de revisión |
|---|---|
| `03_qc_pre_filter.R` | Confirmar cifras pre-filtrado. ¿La muestra `2025017_15_AT_FLOR` (81 % ceros) se marca aquí o en 04? |
| `04_filter_samples.R` | ¿Excluir la muestra del 81 %? ¿con qué criterio replicable? |
| `04b_qc_critical_marks.R` | Marcas críticas presentes en el dataset nuevo |
| `05_sensitivity_sparsity.R` | Recalibrar umbral con 265 peptidoformas |
| `06_filter_peptidoforms.R` y siguientes (06a-06h) | Cada filtro Garcia-lab |
| `07_impute_zeros.R` | CoDA: ¿multiplicativa simple sigue siendo lo correcto? |
| `08_clr_transform.R` | Transformación isométrica |
| `12b_stats_welch_anova.R` | D-022: Welch primario (rec. Delacre 2017) |
| `13c_bootstrap_hedges_ci.R` | D-023: Hedges g + IC95 % (Cumming 2014) |
| `23_ihw_alternative.R` | BH vs IHW |
| `21_plsda.R`, `22_cluster_validation.R` | Validación multivariante |
| `99_render_report.R` | Render final |

**Para cada script:**

1. Leer el código actual juntos.
2. Identificar si el cambio en input invalida supuestos.
3. Decidir si hay que ajustar parámetros (umbrales, etc.).
4. Documentar decisión en acta (`D:/AT_virgen/histone_long_table/decisiones.md`).
5. Ejecutar el target individual.
6. Inspeccionar el rds output.
7. Pasar al siguiente.

### F6 · Re-ejecución completa controlada (sesión 8, ~2 h)

**Objetivo:** `targets::tar_make()` completo desde load_raw hasta report, con todos los targets validados individualmente.

**Entregables:**

- Log completo en `D:/CAP4_NUEVO_OUTPUT/full_rerun_v3.log`
- Inventario de hashes pre/post para auditoría de reproducibilidad
- Tabla comparativa de cifras clave: n peptidoformas en cada filtro, n BH-FDR<0.05, top-10 efectos por contraste

### F7 · Reescritura del cap. 4 v3.0.0 (sesiones 9-10, ~3 h)

**Objetivo:** actualizar `D:/Antigravity/arsenal/_master/capitulo4.qmd` y `D:/CAP4_NUEVO_OUTPUT/reports/cap4.qmd`.

**Cambios esperados:**

- Cifras: 34 muestras (5+11+9+9), 265 peptidoformas pre-filtrado, X peptidoformas post-filtrado (X a determinar)
- Decisiones D-025, D-026, ... que se hayan introducido
- Nuevas figuras con Sistema Visual Pelamovic obligatorio
- Sección "Cambios respecto a v2.0.0" para trazabilidad
- Conclusiones revisadas (en particular las 4 BH-FDR<0.05 en BOT-SEN — ¿se mantienen?)

**Render dual:** HTML + DOCX vía `_quarto.yml`.

### F8 · Control independiente Art. 16 (sesión 11, asíncrono)

**Tribunal de 6 agentes paralelos** (siguiendo el patrón cap. 4 v2.0.0):

1. **Correctitud estadística**: Welch, Hedges g, FDR, supuestos
2. **Reproducibilidad**: pipeline targets, hashes, sessionInfo, paths
3. **Prosa**: anti-AI-writing (writing-rules), ortotipografía, claridad académica
4. **Figuras**: Sistema Visual Pelamovic estricto, colores Okabe-Ito, exportación dual
5. **Coherencia con cap. 3**: nomenclatura, referencias internas, narrativa
6. **Comparativa con literatura**: PXD046034, PXD014739, Garcia-lab benchmarks

**Output:** dictamen `_audit/F9_canon_v3.md` con riesgo % de no cum laude.

### F9 · Cierre y entrega (sesión 12, ~1 h)

- Commit final, tag v3.0.0
- Backup en `D:/Antigravity/arsenal/_master/`
- Update de memoria: `D:/Antigravity/memory/cap4_v3.0.0_handoff.md`
- Update de `MEMORY.md` del usuario

---

## 4. Decisiones críticas pendientes de Pelayo

| Id | Decisión | Recomendación |
|---|---|---|
| Q-1 | ¿La tabla nueva reemplaza al input v2.0.0 o coexiste? | **Reemplaza** (versionando v2.0.0 frozen) |
| Q-2 | ¿Opción A o B en F3 (cargador R)? | **B**: que R lea el CSV largo Python-generado |
| Q-3 | ¿Excluir muestra `2025017_15_AT_FLOR` (81 % ceros)? | Decisión en F5 según criterio Garcia-lab |
| Q-4 | ¿Se hace todo en un sprint o se reparte? | Sugerencia: F1-F4 en un día, F5 en sesiones de 1-2 scripts, F6-F9 al cierre |
| Q-5 | ¿Se preserva el cap. 4 v2.0.0 como capítulo separado o se sustituye? | **Se sustituye** (v2.0.0 frozen como histórico) |

---

## 5. Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Las 4 BH-FDR<0.05 del v2.0.0 desaparecen | Media | Alto | Tener narrativa alternativa preparada en F7 |
| El filtro Garcia-lab elimina la muestra extra y volvemos a 33 | Media | Bajo | Ya está documentado en cap. 4; sólo cambian cifras |
| El parseo Python ha perdido información | Baja | Alto | Sanity checks ya hechos; F1 confirma |
| Aparecen regiones con muy pocas peptidoformas (e.g. H4_79_92 con 1) | Alta | Medio | Filtro `06f_filter_min_peptidoforms` ya lo maneja |
| El usuario quiere acelerar y saltarse F5 paso a paso | Media | Alto | Política: F5 es no negociable; el plan está pensado para esa cadencia |

---

## 6. Estimación de cadencia

- **Sesión 1** (hoy o próxima): F1 + F2 (≈ 2 h)
- **Sesión 2**: F3 + F4 (≈ 2 h)
- **Sesiones 3-7**: F5 paso a paso, 3-5 scripts por sesión (≈ 5 sesiones de 1-2 h)
- **Sesión 8**: F6 ejecución completa (≈ 2 h)
- **Sesiones 9-10**: F7 reescritura cap. 4 (≈ 3 h en total)
- **Sesión 11**: F8 Tribunal Art. 16 (asíncrono)
- **Sesión 12**: F9 cierre (≈ 1 h)

**Total estimado:** 12 sesiones, ~15-20 h de trabajo distribuido en 2-3 semanas reales si se trabaja a buen ritmo.

---

## 7. Próximo paso inmediato

Si validas el plan, mi siguiente acción es:

1. Crear `F1_diff_audit.py` que compara el viejo TSV vs el nuevo a tres niveles (muestras, peptidoformas, valores).
2. Producir `dataset_diff_report.md` con todas las diferencias listadas.
3. Esperar tu lectura del diff antes de tocar nada del pipeline R.

Si quieres ajustes (orden de fases, granularidad de F5, decisiones críticas), respondes y reformulo.
