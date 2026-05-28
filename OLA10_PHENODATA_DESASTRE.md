# 🚨 Hallazgo crítico · phenodata invalida los grupos del pipeline

**Fecha:** 2026-05-26
**Severidad:** BLOQUEANTE ABSOLUTO

## Resumen en 30 segundos

Las etiquetas `YNG`, `BOT`, `FLOR`, `SEN` que aparecen en los nombres de muestra del TSV crudo (`histone_ratios_nucleosoma_completo_para completar.txt`) **son etiquetas placeholder del operador MS, no los grupos biológicos reales**.

El phenodata real (`phenodata_arabidopsis_project.tsv`) revela los grupos correctos. **24 de 32 muestras (75 %) están mal etiquetadas en el pipeline.**

Todo el análisis estadístico del cap. 4 (v3.0.0, v3.1.0, v3.2.0) está construido sobre asignaciones erróneas.

## Grupos REALES (phenodata) vs etiquetas TSV (pipeline)

| Grupo real | n | Grupo TSV asignado (incorrecto) |
|---|---:|---|
| **10H** | 2 | 1× YNG + 1× BOT |
| **14H** | 3 | 1× FLOR + 1× FLOR + 1× SEN |
| **BOT** | 11 | 5× FLOR + 2× SEN + 3× BOT + 1× SEN |
| **FLOR** | 8 | 4× BOT + 3× FLOR + 1× SEN |
| **SEN** | 8 | 4× SEN + 3× BOT + 1× YNG |

**Distribución correcta total**: 10H=2, 14H=3, BOT=11, FLOR=8, SEN=8 → **32 muestras** (5 grupos).

**Distribución asumida por pipeline**: YNG=5, BOT=11, FLOR=9, SEN=9 → 34 muestras (4 grupos).

Discrepancias adicionales:
- **2 muestras del pipeline no aparecen en phenodata**: `sample_index 11` (`2025017_1_AT_YNG`) y `sample_index 15` (`2025017_23_AT_SEN`). Probablemente fallidas técnicamente y descartadas antes del análisis biológico, pero quedaron en el TSV.

## Tabla completa de discrepancias

| sample_index | nombre TSV pipeline | grupo asignado pipeline | grupo REAL phenodata | fecha batch | processing_order |
|---:|---|---|---|---|---:|
| 1  | 2025017_10_AT_YNG  | YNG  | **10H** | 20250506 | 5 |
| 2  | 2025017_11_AT_YNG  | YNG  | **SEN** | 20250506 | 6 |
| 3  | 2025017_12_AT_FLOR | FLOR | **14H** | 20250506 | 7 |
| 4  | 2025017_13_AT_YNG  | YNG  | **BOT** | 20250506 | 8 |
| 5  | 2025017_14_AT_FLOR | FLOR | **BOT** | 20250506 | 9 |
| 6  | 2025017_15_AT_FLOR | FLOR | **BOT** | 20250506 | 10 |
| 7  | 2025017_16_AT_FLOR | FLOR | **BOT** | 20250506 | 11 |
| 8  | 2025017_17_AT_SEN  | SEN  | **BOT** | 20250506 | 12 |
| 9  | 2025017_18_AT_FLOR | FLOR | **14H** | 20250506 | 13 |
| 10 | 2025017_19_AT_SEN  | SEN  | **14H** | 20250506 | 14 |
| 11 | 2025017_1_AT_YNG   | YNG  | _NO está en phenodata_ | — | — |
| 12 | 2025017_20_AT_FLOR | FLOR | FLOR | 20250506 | 16 |
| 13 | 2025017_21_AT_BOT  | BOT  | **10H** | 20250506 | 17 |
| 14 | 2025017_22_AT_BOT  | BOT  | **FLOR** | 20250506 | 18 |
| 15 | 2025017_23_AT_SEN  | SEN  | _NO está en phenodata_ | — | — |
| 16 | 2025017_24_AT_FLOR | FLOR | FLOR | 20250507 | 1 |
| 17 | 2025017_25_AT_BOT  | BOT  | **SEN** | 20250507 | 2 |
| 18 | 2025017_26_AT_SEN  | SEN  | **FLOR** | 20250507 | 3 |
| 19 | 2025017_27_AT_SEN  | SEN  | SEN | 20250507 | 4 |
| 20 | 2025017_28_AT_BOT  | BOT  | **FLOR** | 20250507 | 5 |
| 21 | 2025017_29_AT_BOT  | BOT  | BOT | 20250507 | 6 |
| 22 | 2025017_2_AT_SEN   | SEN  | **BOT** | 20250507 | 7 |
| 23 | 2025017_30_AT_FLOR | FLOR | **SEN** | 20250507 | 8 |
| 24 | 2025017_31_AT_BOT  | BOT  | **FLOR** | 20250507 | 9 |
| 25 | 2025017_32_AT_FLOR | FLOR | **BOT** | 20250507 | 10 |
| 26 | 2025017_33_AT_SEN  | SEN  | SEN | 20250507 | 11 |
| 27 | 2025017_34_AT_SEN  | SEN  | SEN | 20250507 | 12 |
| 28 | 2025017_3_AT_SEN   | SEN  | **BOT** | 20250507 | 13 |
| 29 | 2025017_4_AT_BOT   | BOT  | BOT | 20250507 | 14 |
| 30 | 2025017_5_AT_BOT   | BOT  | **FLOR** | 20250507 | 15 |
| 31 | 2025017_6_AT_BOT   | BOT  | BOT | 20250507 | 16 |
| 32 | 2025017_7_AT_BOT   | BOT  | **FLOR** | 20250507 | 17 |
| 33 | 2025017_8_AT_BOT   | BOT  | **SEN** | 20250507 | 18 |
| 34 | 2025017_9_AT_YNG   | YNG  | **SEN** | 20250507 | 19 |

**Coincidencias**: 8 / 32 (25 %) — los que están en negrita son los 24 discordantes.

## Implicaciones

### 1. Las 4 hits BH-FDR<0.05 del cap. 4 son inválidas

El pipeline calculó stats con grupos {YNG, BOT, FLOR, SEN} arbitrarios. Con grupos reales {10H, 14H, BOT, FLOR, SEN}:
- El contraste "BOT_vs_SEN" mezclaba muestras reales BOT+FLOR+SEN+10H+14H del pipeline
- El contraste "FLOR_vs_SEN" mezclaba aún más
- Resultados de las 4 peptidoformas BH-FDR<0.05 son **artefactos numéricos sin base biológica**

### 2. Batch effect real no modelado

Dos fechas de adquisición MS:
- **20250506**: 14 muestras (samples 1-14 del processing order del 06/05)
- **20250507**: 18 muestras (samples ATSEN*, ATBOTON*, ATFLOR* del 07/05)

Los grupos no están equilibrados por fecha. Hay efecto temporal técnico que se debe corregir con `limma::removeBatchEffect()` o ComBat o como covariable en los modelos.

### 3. Processing_order disponible para corrección de drift LC

Cada muestra tiene su orden de inyección (1-19 dentro de cada batch). Permite modelar drift cromatográfico si fuera necesario (probablemente innecesario tras corrección por batch).

### 4. El cap. 3 también está mal

El cap. 3 declaraba YNG/BOT/FLOR/SEN con DAS 21-25/28-32/35-42/45-55. Los grupos reales son 10H/14H/BOT/FLOR/SEN — la nomenclatura de fotoperíodo (10H, 14H) no encaja con DAS.

## Pregunta crítica para Pelayo

**¿Cuál es la verdad biológica del experimento?**

Opción A: **Los grupos reales son 10H/14H/BOT/FLOR/SEN** (lo que dice el phenodata). En este caso:
- Las etiquetas YNG del TSV son errores tipográficos del operador
- "10H" y "14H" probablemente refieren a fotoperíodos (10 h vs 14 h luz)
- 10H+14H combinados = "Juvenil" antes de bolting (5 muestras)
- El cap. 4 necesita rehacerse con la asignación correcta

Opción B: **YNG = 10H+14H** combinado intencionalmente
- La agrupación del pipeline (5 muestras YNG) coincide con 10H+14H sumadas (2+3=5)
- Pero solo 1 sample_index (el 1) coincide en el mapping YNG↔10H/14H; los demás 24 son discordantes
- Por tanto esta opción NO es consistente con los datos

Opción C: **Hay un error en el phenodata**
- El phenodata refleja otra cohorte
- Muy improbable porque coincide el lote 2025017 y fechas 20250506/07

## Recomendación

**STOP en cap. 4 v3.2.0**. La verdad canónica D-034 (4 hits BOT_vs_SEN) es inválida.

**Plan obligatorio antes de continuar:**

1. **Pelayo confirma** los grupos biológicos reales (Opción A más probable).
2. **Re-cargar** la tabla maestra con grupos del phenodata (no del TSV).
3. **Excluir** las 2 muestras sin phenodata (sample_index 11 y 15).
4. **Diseño experimental** con 5 grupos {10H, 14H, BOT, FLOR, SEN} y batch_date como covariable.
5. **Re-correr stats** con corrección por batch (limma::removeBatchEffect previo a CLR, o batch como covariable en Welch/lm).
6. **Re-derivar hits BH-FDR<0.05** — probablemente serán distintos.
7. **Reescribir cap. 4** completamente con la verdad biológica.

## Estado del repo

- Tag v3.2.0 firmado y push a GitHub **debe quedarse como histórico** (con etiquetas placeholder del TSV).
- Crear nueva rama `v4.0.0-phenodata-correction` para la corrección biológica.
- O bien etiquetar el v3.2.0 como "WITHDRAWN: phenodata mismatch detected" y avanzar a v4.0.0.

## Acción inmediata sugerida

```bash
# 1. Confirmar grupos con Pelayo (humano).
# 2. Si Opción A: rehacer build_long_table.py para que el grupo venga del
#    phenodata, no del nombre del TSV.
# 3. Re-correr pipeline R/targets desde load_raw.
# 4. Tribunal Art. 16 v4 sobre el nuevo cap. 4.
```

Esto **invalida 4 meses de trabajo previo del cap. 4**. Pero es la única manera honesta de defender la tesis.
