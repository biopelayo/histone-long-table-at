# OLA 4 · Reescritura propuesta del capítulo 3

**Fecha:** 2026-05-25
**Autor:** Pelayo González de Lena Rodríguez con asistencia Claude (Opus 4.7, 1M ctx)
**Estado:** propuesta de reescritura en Markdown. NO toca `CHAPTER_METHODS_rev_1604_LV.docx` ni `capitulo4.qmd`.
**Resuelve:** BLOQ-7 del Tribunal Art. 16 (Capa T5).
**Fuente de verdad para el contraste y los 4 hits:** `T_verdad_4hits.{csv,md}` v1.0.0.
**Fuente de verdad para el catálogo de peptidoformas:** `docs/094_PEPTIDOFORM_MASTER_LIST.md`.

Aplica writing-rules de `D:\Antigravity\memory\writing_rules.md` y constitución Pelamovic Art. 16.

---

## §2.1.2 Diseño experimental (REESCRITO)

El lote biológico **2025017** comprende plantas de *Arabidopsis thaliana* Col-0 cultivadas en cámara de cultivo bajo condiciones controladas y muestreadas en cuatro estadios cronológicos del desarrollo de la roseta. La asignación de estadio a días tras la siembra (DAS) sigue las descripciones fenológicas de Boyes et al. (2001) sobre Col-0 en cámara y la cartografía transcriptómica de Klepikova et al. (2016) para la zona vegetativa-reproductiva:

| Estadio | Etiqueta | DAS | Fenotipo característico |
|---|---|:---:|---|
| Juvenil | YNG | 21-25 | Roseta vegetativa, 6-8 hojas |
| Comienzo del *bolting* | BOT | 28-32 | Emergencia del tallo floral (< 1 cm) |
| Floración | FLOR | 35-42 | Antesis de las primeras flores |
| Senescencia foliar | SEN | 45-55 | Hojas basales amarillentas, silicuas en desarrollo |

: Estadios del lote 2025017. {#tbl-3-1-diseno}

El lote de partida contiene **34 muestras** distribuidas en YNG (n = 5), BOT (n = 11), FLOR (n = 9) y SEN (n = 9). Cada muestra es una réplica biológica independiente: una planta única cuya parte aérea se recolectó al estadio asignado, se congeló en N₂ líquido y se procesó de forma individual a lo largo de toda la cadena experimental.

Tras el control de calidad composicional descrito en §3.X.Y, se excluye la muestra `2025017_15_AT_FLOR` por presentar **sparsity composicional del 80,7 %** (proporción de peptidoformas con valor 0 sobre el catálogo completo), criterio operativo D-002 documentado en el capítulo 4. El catálogo retenido para los análisis estadísticos del capítulo 4 es por tanto de **33 muestras** con la distribución YNG = 5, BOT = 11, FLOR = 8 y SEN = 9.

El desbalance entre estadios (razón 1 : 2,2 entre el grupo menor y el mayor) es consecuencia operativa del cronograma de muestreo, no fruto de pérdidas analíticas. Esta asimetría condiciona la elección del test ómnibus paramétrico del capítulo 4 (Welch-ANOVA sin homocedasticidad, decisión D-022).

**Referencias añadidas en bibliografía:**

- Boyes DC et al. (2001) *Plant Cell* 13: 1499-1510. Growth stage-based phenotypic analysis of *Arabidopsis*.
- Klepikova AV et al. (2016) *Plant J* 88: 1058-1070. A high resolution map of the *Arabidopsis thaliana* developmental transcriptome.

---

## §3.B Catálogo histónico (SECCIÓN AÑADIDA)

El bundle EpiProfile-PLANTS aplicado al lote 2025017 cuantifica **265 peptidoformas** sobre 40 péptidos canónicos distribuidos en 33 regiones histónicas. El catálogo distribuido por familia histónica es el siguiente:

| Familia | PF | Péptidos representativos | Variantes / observaciones |
|---|:---:|---|---|
| H1 | 6 | KLLLLNLKR, TGSSQYAIQKFIEEKR, KLLLVNLKR, TGSSQYAIQKFIEEKHKSLPPTFR | Plan H1 reducido a 4 layouts AT verificados (`HH1_AT01`-`HH1_AT04`) tras Tier 4 |
| H2A | 22 | SSKAGLQFPVGR (Can+X), GKTLGSGSAKKATTR (Can1), AGIQFPVGR (Z), GKPKATKSVSR (X), FLKSGKYAER (Xa), SGGGPKKKPVSR (W12), SVKSGLQFPVGR (W12), MESTGKVKKAFGGR (W6) | Cubre canónica + 5 variantes (W6, W12, X, Xa, Z); incluye octeto diagnóstico HH2A_01u |
| H2B | 13 | EIQTAVR (shared), YNKKPTITSR (shared), LVLPGELAKHAVSEGTK (shared), IFEKLA[SQGQ]ESSKLAR (4 variantes disc.) | Cuatro péptidos discriminantes de variantes H2B (`H2B4`-`H2B7`) |
| H3 | 37 | TKQTAR, KSTGGKAPR (+S10ph, +S10ac), KQLATKAAR, **KSAPATGGVKKPHR** (H3.1, 27-40), YRPGTVALR, KYQKSTELLIR, **EIAQDFKTDLR** (73-83), VTIMPKDIQLAR | Layouts `H3_01` a `H3_08` |
| H3.3 | 10 | **KSAPTTGGVKKPHR** (H3.3, 27-40) | Layout `H33_27_40` exclusivo de H3.3; el resto de péptidos H3.3 es indistinguible de H3.1 por *bottom-up* |
| H4 | 9 | GKGGKGLGKGGAKR (4-17), **KVLR** (20-23), RGGVKR (40-45), KTVTAMDVVYALKR (79-92) | H4_4_17 agregado por número de acetilaciones (D-018) |
| **Total** | **97** | | Cifra **post-filtros Garcia-lab + D-024** |

: Catálogo histónico AT operativo en cap. 3 y cap. 4. PF = peptidoformas tras filtros. {#tbl-3-B-catalogo}

**Cifras clave:**

- 265 peptidoformas pre-filtrado (output bruto EpiProfile-PLANTS).
- 97 peptidoformas post-filtrado (cifra defendida en cap. 4, decisión D-003 y §4.1.3).
- 33 regiones histónicas con al menos un péptido canónico.
- Cobertura H3, H4, H1 completa; H2A y H2B cubren todas las variantes con péptido tríptico ≥ 6 residuos.

### Glosario nomenclatura H2A

Las etiquetas de variantes H2A usadas en cap. 3 y cap. 4 siguen la convención del consorcio EpiProfile-PLANTS:

| Etiqueta | Variante AT | Función biológica reportada |
|---|---|---|
| Can | H2A canónica (HTA1-3) | Forma mayoritaria, cromatina activa |
| W6 | H2A.W (HTA6) | Heterocromatina constitutiva, dominio C-terminal SQ |
| W12 | H2A.W (HTA12, HTA9) | Heterocromatina, dominio SQ extendido |
| X | H2A.X (HTA3, HTA5) | Respuesta a daño en DNA (γH2A.X) |
| Xa | H2A.X variante α | Subforma transcripcionalmente activa |
| Z | H2A.Z (HTA8, HTA9, HTA11) | Bivalente promotor/silenciamiento, regulación termosensible |

: Variantes H2A en *A. thaliana* y nomenclatura operativa. {#tbl-3-B-h2a}

### Discriminación H3.1 vs H3.3

H3.1 y H3.3 difieren en cuatro residuos en la secuencia primaria de Col-0. Por **bottom-up con tripsina + propionilación**, la región 27-40 produce dos péptidos distintos por una sustitución A↔T en posición 31:

- **H3.1**: `KSAPATGGVKKPHR` (Ala31), layout `H3_27_40`.
- **H3.3**: `KSAPTTGGVKKPHR` (Thr31), layout `H33_27_40`.

El resto del esqueleto H3 (péptidos 9-17, 18-26, 41-49, 53-63, 73-83, 117-128) es idéntico entre las dos variantes y **no permite discriminación variante-específica** con el método actual. Por convención, las peptidoformas cuantificadas sobre estos péptidos compartidos se reportan como «H3 (compartida)» en cap. 4. La cuantificación variante-específica del par 27-40 es la pieza clave del análisis ontogénico H3.1/H3.3 en BOT-SEN.

---

## §3.X Cuantificación de H3K79 (SECCIÓN NUEVA)

La modificación H3K79 (mono-, di- y trimetilación; acetilación) se cuantifica sobre el péptido **EIAQDFKTDLR** correspondiente a los residuos **73-83** de H3, layout `H3_07_73_83` del bundle EpiProfile-PLANTS.

| Layout | Péptido | Posición | Peptidoformas |
|---|---|:---:|---|
| `H3_07_73_83` | EIAQDFKTDLR | 73-83 (H3.1/H3.3) | unmod, K79me1, K79me2, K79me3, K79ac |

Las cinco peptidoformas cuantificadas se han validado en el primer análisis del lote 2025017 (2026-04-06) sobre 34 RAWs. El layout es estable tras la revisión Tier (tier 1, sin correcciones requeridas; ver `docs/087_TIER_MASTER_LIST.md`). La discriminación H3.1/H3.3 sobre este péptido es **nula** porque los residuos 73-83 son idénticos entre las dos variantes; la cuantificación se reporta como H3 (compartida).

### Justificación biológica

H3K79 ocupa una posición funcional en el núcleo globular del nucleosoma, no en la cola N-terminal. Es marcador clásico de eucromatina activa y de la actividad de la metiltransferasa DOT1L en metazoos; en plantas, el papel funcional es menos conocido pero está documentado:

- **Wood, Tellier y Murphy (2018)** revisan el papel de DOT1L y H3K79me en transcripción activa en eucariotas y discuten su conservación funcional.
- **Steger et al. (2008)** caracterizan H3K79me como marca asociada a elongación transcripcional por RNA Pol II.
- **Liu et al. (2010)** documentan H3K79me en *A. thaliana* y su distribución genómica a lo largo del cuerpo de genes activos.

La inclusión de H3K79 en el catálogo del lote 2025017 amplía el panel de marcas de eucromatina más allá de H3K4me y H3K36me (ambas presentes en el catálogo del cap. 4).

**Referencias añadidas:**

- Wood K, Tellier M, Murphy S (2018) *Biomolecules* 8: 11. DOT1L and H3K79 methylation in transcription and genomic stability.
- Steger DJ et al. (2008) *Mol Cell Biol* 28: 2825-2839. DOT1L/KMT4 recruitment and H3K79 methylation are ubiquitously coupled with gene transcription in mammalian cells.
- Liu C et al. (2010) *PLoS One* 5: e12856. Genome-wide chromatin profiling reveals dynamic remodeling of H3K27me3 and H3K79me1 during Arabidopsis flowering.

---

## Unificación de grafía: `EpiProfile-PLANTS`

Toda mención al bundle de cuantificación adopta la grafía **kebab-case** `EpiProfile-PLANTS` en ambos capítulos. Se eliminan las variantes `EpiProfile_PLANTS`, `EpiProfile PLANTS`, `epiProfilePlants` y similares. La grafía vinculante es la registrada en el repositorio canónico (`github.com/biopelayo/epiprofile-plants`).

Acciones concretas en cap. 3:

- Buscar y reemplazar todas las ocurrencias de `EpiProfile_PLANTS` → `EpiProfile-PLANTS`.
- Igual en figuras (subtítulos, leyendas), tablas y notas a pie.
- Igual en el README del bundle si la grafía no está unificada.

---

## Limpieza del borrador `CHAPTER_METHODS_rev_1604_LV.docx`

### Eliminación de notas embebidas del codirector LV

El borrador contiene comentarios revisores embebidos en el cuerpo (probablemente `Track Changes` resueltos como texto plano y notas marginales transferidas en línea). Acciones:

1. Aceptar o rechazar todos los cambios con `Track Changes` en Word antes de exportar.
2. Trasladar las preguntas abiertas de LV a un fichero `cap3_notas_LV.md` aparte; resolverlas con LV en sesión presencial antes del envío.
3. Eliminar todo bloque con prefijo `[LV:`, `[Comentario LV]`, `[?]`, o equivalente.

### Tablas con numeración rota

El tribunal detectó referencias a `Table 245` y similares, signo de campos cruzados rotos. Acciones:

1. Regenerar todas las referencias cruzadas a tablas (`Update Field` global en Word, o reconstrucción manual).
2. Renumerar de forma secuencial: 3.1, 3.2, 3.3, ... dentro del capítulo.
3. Verificar referencias internas en el texto («ver Tabla 3.2», «como se muestra en la Tabla 3.4»).

### Sección placeholder

Cualquier sección con encabezado pero cuerpo vacío o con marcas `[completar]`, `[TODO]`, `[pendiente]` se completa antes del envío. Lista mínima a verificar:

- §2.1 Material vegetal (DAS, cámara, fotoperíodo, intensidad lumínica).
- §2.2 Extracción de histonas (volúmenes, tiempos, temperaturas).
- §2.3 Propionilación (anhídrido propiónico, ratio, número de rondas).
- §2.4 Digestión (relación tripsina/sustrato, tiempo, temperatura).
- §2.5 LC--MS/MS (gradiente, columna, parámetros del ZenoTOF 7600).
- §2.6 EpiProfile-PLANTS (versión, parámetros, hardware, tiempo de cómputo).
- §2.7 Filtros Garcia-lab y composicionales (alineado con cap. 4 §4.2, decisiones D-014 a D-024).

### Decisión D-029: política lingüística del capítulo

El capítulo 4 está en castellano de España. El cap. 3 actual está en inglés. **Decisión propuesta D-029**: traducir el cap. 3 íntegro al castellano de España y aplicar las 15 decisiones canónicas de ortotipografía (cursivas para *A. thaliana* y *Col-0*, et al. en redonda, LC--MS/MS con en-dash, MS1/MS2 sin superíndice, coma decimal, espacio fino para miles, espacio antes de %, comillas latinas «», anglicismos en cursiva la primera vez).

Justificación: coherencia con el resto del manuscrito y con la política de la Universidad de Oviedo para tesis con mención internacional opcional (resumen y conclusiones en inglés a parte, cuerpo en castellano).

---

## Lista de eliminaciones propuestas del cap. 3 actual

El borrador menciona organismos modelo o variantes no usadas en el análisis del lote 2025017. Para evitar inconsistencias cap. 3 ↔ cap. 4 (capa T5 del tribunal), se proponen las siguientes eliminaciones:

| Tema | Acción | Razón |
|---|---|---|
| *Marchantia polymorpha* | Eliminar mención salvo si se usa como referencia metodológica explícita | Fuera del alcance del lote 2025017 |
| *Chlamydomonas reinhardtii* | Eliminar | No es planta vascular, no aplica al protocolo AT |
| H3_06a_53_63 (RYQKSTELLIR) | Mantener solo en el apéndice de variantes; no en cuerpo | `display = 0` por *missed cleavage* (ver `087_TIER_MASTER_LIST.md`) |
| H2A heavy/N15/SILAC (HH2AH_*, HH2AN_*, HH2AMo_*) | Eliminar | Tier 4, no usadas en lote 2025017 |
| Funciones SILAC genéricas | Eliminar | El lote no usa marcaje isotópico |
| Mención a `H3_17_73_83` para K79 | Sustituir por `H3_07_73_83` | `H3_17` cuantifica variantes de secuencia, no PTMs |

---

## Coherencia 4-hits con cap. 4 (Capa T5 del tribunal)

El cap. 3 no reporta resultados estadísticos. Sí debe documentar **el contrato** con el cap. 4:

- Los hallazgos **BH-FDR < 0,05** del cap. 4 v3.1.0 se concentran en el **contraste BOT vs SEN** y abarcan cuatro peptidoformas:

  | Peptidoforma | Péptido | log2FC | Cohen *d* | FDR-BH |
  |---|---|---:|---:|---:|
  | H3_27_40 K27me2 | KSAPATGGVKKPHR | −1,142 | −2,148 | 0,01746 |
  | H4_20_23 K20me1 | KVLR | 1,714 | 1,86 | 0,01746 |
  | H3_27_40 unmod | KSAPATGGVKKPHR | 2,177 | 2,046 | 0,03510 |
  | H4_20_23 K20me2 | KVLR | −3,436 | −1,557 | 0,03599 |

  : Verdad canónica de hallazgos del cap. 4 v3.1.0. Fuente: `T_verdad_4hits.csv`. {#tbl-3-T5-coherencia}

- El cap. 3 no reescribe estos resultados; cita esta tabla y remite a §4.6 y §4.9 del cap. 4.
- El cap. 3 explicita que el contraste con resolución estadística suficiente bajo el desbalance n = 5/11/8/9 es **BOT-SEN**, no FLOR-SEN ni transiciones intermedias.

---

## Decisiones nuevas propuestas

| Id | Decisión | Sección | Estado |
|---|---|---|:---:|
| **D-029** | Cap. 3 en castellano de España completo | §3.0 | propuesta |
| **D-030** | Grafía vinculante `EpiProfile-PLANTS` (kebab-case) | §3.0 | propuesta |
| **D-031** | Catálogo histónico de §3.B como tabla canónica para cap. 4 | §3.B | propuesta |
| **D-032** | H3K79 sobre layout `H3_07_73_83` (no `H3_17`) | §3.X | propuesta |
| **D-033** | DAS por estadio según Boyes 2001 + Klepikova 2016 | §3.2.1 | propuesta |

---

## Próximos pasos

1. Pelayo lee este MD, decide si acepta la traducción al castellano (D-029) y la inclusión de §3.B y §3.X.
2. Pelayo aplica los cambios al `CHAPTER_METHODS_rev_1604_LV.docx` (no este agente).
3. Sesión presencial con LV para resolver notas embebidas y validar la nueva estructura del capítulo.
4. Tras la sesión, render dual `.docx` + `.html` desde Quarto si el cap. 3 se migra a `.qmd`.
5. Verificación cruzada cap. 3 ↔ cap. 4 con script `tests/test_cross_chapter_consistency.py`.

---

## Trazabilidad

- Fuente del contraste y los 4 hits: `D:/AT_virgen/histone_long_table/T_verdad_4hits.csv` v1.0.0.
- Fuente del catálogo: `D:/AT_virgen/docs/094_PEPTIDOFORM_MASTER_LIST.md`.
- Fuente de los Tiers: `D:/AT_virgen/docs/087_TIER_MASTER_LIST.md`.
- Layout H3K79: `D:/AT_virgen/docs/033_H3_17_73_83.md` (variantes de secuencia, no PTMs; el layout PTMs K79 corresponde a `H3_07_73_83`).
- Tribunal T5: `D:/AT_virgen/histone_long_table/F8_tribunal_consolidado.md`.
- Texto-base del cap. 4 que coordina con el cap. 3: `D:/Antigravity/arsenal/_master/sections/41_datos.qmd` y `4C_decisiones.qmd`.
