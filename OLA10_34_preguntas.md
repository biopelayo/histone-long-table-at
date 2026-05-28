# Phenodata v4.0 desde cero · 34 preguntas, una por muestra

**Instrucciones:** revisa cada muestra. Para cada una necesito:
- **grupo biológico real** (e.g. 10H, 14H, BOT, FLOR, SEN, o el que sea correcto)
- **batch / fecha** (20250506 o 20250507; o "DESCARTAR" si fue fallida)
- **processing_order** (opcional, si lo tienes)
- **notas** (opcional: técnica, comentarios)

Para responder rápido, puedes:
- Decir `OK todas` si la columna *hipótesis* está bien
- Decir `corrección N: grupo=X, batch=Y` por las que estén mal
- O pegarme una tabla con las 34 filas rellenas

---

**Contexto que conozco**:
- TSV crudo tiene 34 columnas-muestra con etiquetas tipo `2025017_X_AT_YYY` donde YYY es lo que escribió el operador (placeholder, NO confiable).
- Phenodata previo (que dijiste que está mal) tenía 32 entradas + 2 huérfanas.
- Hay 2 fechas de adquisición MS: 20250506 y 20250507.

---

## Pregunta 1 · sample_index = 1
- **Etiqueta TSV**: `2025017_10_AT_YNG`
- **biorep_id según TSV**: 10
- Hipótesis previa: grupo=10H, batch=20250506, processing=5, code=10H_1
- **¿Grupo biológico real?** ___
- **¿Batch (fecha)?** ___
- **¿Notas?** ___

## Pregunta 2 · sample_index = 2
- **Etiqueta TSV**: `2025017_11_AT_YNG`
- **biorep_id según TSV**: 11
- Hipótesis previa: grupo=SEN, batch=20250506, processing=6, code=SEN_1
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 3 · sample_index = 3
- **Etiqueta TSV**: `2025017_12_AT_FLOR`
- **biorep_id según TSV**: 12
- Hipótesis previa: grupo=14H, batch=20250506, processing=7, code=14H_1
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 4 · sample_index = 4
- **Etiqueta TSV**: `2025017_13_AT_YNG`
- **biorep_id según TSV**: 13
- Hipótesis previa: grupo=BOT, batch=20250506, processing=8, code=BOT_1
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 5 · sample_index = 5
- **Etiqueta TSV**: `2025017_14_AT_FLOR`
- **biorep_id según TSV**: 14
- Hipótesis previa: grupo=BOT, batch=20250506, processing=9, code=BOT_2
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 6 · sample_index = 6
- **Etiqueta TSV**: `2025017_15_AT_FLOR`
- **biorep_id según TSV**: 15
- Hipótesis previa: grupo=BOT, batch=20250506, processing=10, code=BOT_3
- *Nota técnica*: esta muestra tenía 81 % de ceros en mi QA previo — ¿fallida?
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 7 · sample_index = 7
- **Etiqueta TSV**: `2025017_16_AT_FLOR`
- **biorep_id según TSV**: 16
- Hipótesis previa: grupo=BOT, batch=20250506, processing=11, code=BOT_4
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 8 · sample_index = 8
- **Etiqueta TSV**: `2025017_17_AT_SEN`
- **biorep_id según TSV**: 17
- Hipótesis previa: grupo=BOT, batch=20250506, processing=12, code=BOT_5
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 9 · sample_index = 9
- **Etiqueta TSV**: `2025017_18_AT_FLOR`
- **biorep_id según TSV**: 18
- Hipótesis previa: grupo=14H, batch=20250506, processing=13, code=14H_2
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 10 · sample_index = 10
- **Etiqueta TSV**: `2025017_19_AT_SEN`
- **biorep_id según TSV**: 19
- Hipótesis previa: grupo=14H, batch=20250506, processing=14, code=14H_3
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 11 · sample_index = 11 ⚠ HUÉRFANA
- **Etiqueta TSV**: `2025017_1_AT_YNG`
- **biorep_id según TSV**: 1
- *NO aparece en el phenodata previo*
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Está fallida o se debe incluir?** ___
- **¿Notas?** ___

## Pregunta 12 · sample_index = 12
- **Etiqueta TSV**: `2025017_20_AT_FLOR`
- **biorep_id según TSV**: 20
- Hipótesis previa: grupo=FLOR, batch=20250506, processing=16, code=FLOR_1
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 13 · sample_index = 13
- **Etiqueta TSV**: `2025017_21_AT_BOT`
- **biorep_id según TSV**: 21
- Hipótesis previa: grupo=10H, batch=20250506, processing=17, code=10H_2
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 14 · sample_index = 14
- **Etiqueta TSV**: `2025017_22_AT_BOT`
- **biorep_id según TSV**: 22
- Hipótesis previa: grupo=FLOR, batch=20250506, processing=18, code=FLOR_2
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 15 · sample_index = 15 ⚠ HUÉRFANA
- **Etiqueta TSV**: `2025017_23_AT_SEN`
- **biorep_id según TSV**: 23
- *NO aparece en el phenodata previo*
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Está fallida o se debe incluir?** ___
- **¿Notas?** ___

## Pregunta 16 · sample_index = 16
- **Etiqueta TSV**: `2025017_24_AT_FLOR`
- **biorep_id según TSV**: 24
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=1, code=FLOR_7
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 17 · sample_index = 17
- **Etiqueta TSV**: `2025017_25_AT_BOT`
- **biorep_id según TSV**: 25
- Hipótesis previa: grupo=SEN, batch=20250507, processing=2, code=SEN_2
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 18 · sample_index = 18
- **Etiqueta TSV**: `2025017_26_AT_SEN`
- **biorep_id según TSV**: 26
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=3, code=FLOR_9
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 19 · sample_index = 19
- **Etiqueta TSV**: `2025017_27_AT_SEN`
- **biorep_id según TSV**: 27
- Hipótesis previa: grupo=SEN, batch=20250507, processing=4, code=SEN_4
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 20 · sample_index = 20
- **Etiqueta TSV**: `2025017_28_AT_BOT`
- **biorep_id según TSV**: 28
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=5, code=FLOR_4
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 21 · sample_index = 21
- **Etiqueta TSV**: `2025017_29_AT_BOT`
- **biorep_id según TSV**: 29
- Hipótesis previa: grupo=BOT, batch=20250507, processing=6, code=BOT_6
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 22 · sample_index = 22
- **Etiqueta TSV**: `2025017_2_AT_SEN`
- **biorep_id según TSV**: 2
- Hipótesis previa: grupo=BOT, batch=20250507, processing=7, code=BOT_10
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 23 · sample_index = 23
- **Etiqueta TSV**: `2025017_30_AT_FLOR`
- **biorep_id según TSV**: 30
- Hipótesis previa: grupo=SEN, batch=20250507, processing=8, code=SEN_8
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 24 · sample_index = 24
- **Etiqueta TSV**: `2025017_31_AT_BOT`
- **biorep_id según TSV**: 31
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=9, code=FLOR_6
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 25 · sample_index = 25
- **Etiqueta TSV**: `2025017_32_AT_FLOR`
- **biorep_id según TSV**: 32
- Hipótesis previa: grupo=BOT, batch=20250507, processing=10, code=BOT_8
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 26 · sample_index = 26
- **Etiqueta TSV**: `2025017_33_AT_SEN`
- **biorep_id según TSV**: 33
- Hipótesis previa: grupo=SEN, batch=20250507, processing=11, code=SEN_3
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 27 · sample_index = 27
- **Etiqueta TSV**: `2025017_34_AT_SEN`
- **biorep_id según TSV**: 34
- Hipótesis previa: grupo=SEN, batch=20250507, processing=12, code=SEN_6
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 28 · sample_index = 28
- **Etiqueta TSV**: `2025017_3_AT_SEN`
- **biorep_id según TSV**: 3
- Hipótesis previa: grupo=BOT, batch=20250507, processing=13, code=BOT_7
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 29 · sample_index = 29
- **Etiqueta TSV**: `2025017_4_AT_BOT`
- **biorep_id según TSV**: 4
- Hipótesis previa: grupo=BOT, batch=20250507, processing=14, code=BOT_9
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 30 · sample_index = 30
- **Etiqueta TSV**: `2025017_5_AT_BOT`
- **biorep_id según TSV**: 5
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=15, code=FLOR_5
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 31 · sample_index = 31
- **Etiqueta TSV**: `2025017_6_AT_BOT`
- **biorep_id según TSV**: 6
- Hipótesis previa: grupo=BOT, batch=20250507, processing=16, code=BOT_11
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 32 · sample_index = 32
- **Etiqueta TSV**: `2025017_7_AT_BOT`
- **biorep_id según TSV**: 7
- Hipótesis previa: grupo=FLOR, batch=20250507, processing=17, code=FLOR_8
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 33 · sample_index = 33
- **Etiqueta TSV**: `2025017_8_AT_BOT`
- **biorep_id según TSV**: 8
- Hipótesis previa: grupo=SEN, batch=20250507, processing=18, code=SEN_5
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

## Pregunta 34 · sample_index = 34
- **Etiqueta TSV**: `2025017_9_AT_YNG`
- **biorep_id según TSV**: 9
- Hipótesis previa: grupo=SEN, batch=20250507, processing=19, code=SEN_7
- **¿Grupo real?** ___
- **¿Batch?** ___
- **¿Notas?** ___

---

## Preguntas globales antes de empezar

**G1.** ¿Los grupos biológicos son `{10H, 14H, BOT, FLOR, SEN}` o algo distinto (e.g. juvenil/adulto en lugar de 10H/14H)?

**G2.** ¿Las 2 huérfanas (sample_index 11 y 15) son fallos técnicos a descartar, o entran en el análisis?

**G3.** ¿Tienes el conteo correcto por grupo final? (e.g. n_10H=2, n_14H=3, n_BOT=11, n_FLOR=8, n_SEN=8 o distinto)

**G4.** ¿Confirmas que el batch técnico es exactamente la fecha de adquisición (20250506 vs 20250507) y nada más (no hay sub-batches de columna LC, día de preparación de muestra, etc.)?

**G5.** ¿El processing_order es importante para nosotros o lo dejamos solo como variable observacional?

---

## Plantilla CSV alternativa para que rellenes en bloque

Si prefieres editar una tabla en lugar de responder en formato largo, copia esto en Excel/CSV y devuélvemelo relleno:

```csv
sample_index,tsv_name,biorep,group_real,batch,processing_order,notes
1,2025017_10_AT_YNG,10,,,,
2,2025017_11_AT_YNG,11,,,,
3,2025017_12_AT_FLOR,12,,,,
4,2025017_13_AT_YNG,13,,,,
5,2025017_14_AT_FLOR,14,,,,
6,2025017_15_AT_FLOR,15,,,,
7,2025017_16_AT_FLOR,16,,,,
8,2025017_17_AT_SEN,17,,,,
9,2025017_18_AT_FLOR,18,,,,
10,2025017_19_AT_SEN,19,,,,
11,2025017_1_AT_YNG,1,,,,
12,2025017_20_AT_FLOR,20,,,,
13,2025017_21_AT_BOT,21,,,,
14,2025017_22_AT_BOT,22,,,,
15,2025017_23_AT_SEN,23,,,,
16,2025017_24_AT_FLOR,24,,,,
17,2025017_25_AT_BOT,25,,,,
18,2025017_26_AT_SEN,26,,,,
19,2025017_27_AT_SEN,27,,,,
20,2025017_28_AT_BOT,28,,,,
21,2025017_29_AT_BOT,29,,,,
22,2025017_2_AT_SEN,2,,,,
23,2025017_30_AT_FLOR,30,,,,
24,2025017_31_AT_BOT,31,,,,
25,2025017_32_AT_FLOR,32,,,,
26,2025017_33_AT_SEN,33,,,,
27,2025017_34_AT_SEN,34,,,,
28,2025017_3_AT_SEN,3,,,,
29,2025017_4_AT_BOT,4,,,,
30,2025017_5_AT_BOT,5,,,,
31,2025017_6_AT_BOT,6,,,,
32,2025017_7_AT_BOT,7,,,,
33,2025017_8_AT_BOT,8,,,,
34,2025017_9_AT_YNG,9,,,,
```
