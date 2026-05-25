# OLA 6 · Consolidación bibliográfica del Capítulo 4

**Fecha:** 2026-05-25. **Operador:** bibliógrafo Art. 16.
**Archivo modificado:** `D:/CAP4_NUEVO_OUTPUT/references.bib`.

## 1. Inventario inicial vs final

| Conteo | Entradas BibTeX | Origen |
|---|---:|---|
| Antes (v3.0.0) | 33 | versión heredada del megamaster 2026-05-11 |
| Después (OLA 6) | **84** | 33 + 51 nuevas (≥65 exigidas: cumplido con margen) |

Cobertura por bloque temático: CoDA fundamentos (8), proteómica bottom-up Garcia/Sidoli/Yuan/Lochmanová/Ryzhaya (12), cromatina vegetal y variantes (12), senescencia y heterocromatina (6), H3K79/DOT1L/SDG (5), H2B ubiquitinación + H1 linker (8), fenología y transcriptómica (5), estadística inferencial (8), FAIR + autocita (2).

## 2. Citas presentes pero NO citadas (huérfanas, candidatas a eliminar)

Detectadas en el `.bib` heredado, sin uso en `cap4.qmd`, `capitulo4.qmd` ni sus 13 sections includes:

- `pearson1897` — citada **una sola vez** en `48_redes.qmd` (§4.8 intro composicional). Se mantiene anclada en esa sección.
- `tukey1949` — no citada en ningún archivo. **Candidata a eliminar** en próxima limpieza (no ejecutada en esta ola para preservar la entrada como precedente histórico del ANOVA, por si se reactiva el Apéndice 4.A.1).
- `sandve2013` — no citada. **Candidata a eliminar** o a anclar en §4.D (Reproducibilidad) si se desea sostener el principio de "Ten Simple Rules".

No se elimina ninguna entrada en esta ola para preservar trazabilidad. Decisión diferida al siguiente sprint.

## 3. Citas en prosa que requieren cambio a sintaxis `[@key]`

El cuerpo del capítulo cita exclusivamente en formato APA en prosa (`Aitchison, 1986`; `Pawlowsky-Glahn et al. 2015`). Ninguna sección usa todavía la sintaxis Pandoc `[@key]` con la `.bib`. Reportadas como **pendientes de migración** (NO se han modificado los `.qmd`):

### Citas presentes en `cap4.qmd` (reports/) y `capitulo4.qmd` (master)

`aitchison1986`, `pawlowsky2015`, `egozcue2003`, `martinFernandez2015`, `palarea2015`, `gloor2017`, `lovell2015`, `welch1947`, `bh1995`, `delacre2017`, `cumming2014`, `cohen1988`, `hedges1981`, `efron1993`, `ignatiadis2016`, `smithson2006`, `tibshirani2001`, `suzuki2006`, `rousseeuw1987`, `diCiccio1996`, `gelmanRubin1992`, `garcia2007`, `sidoli2014`, `sidoli2016`, `sidoliGarcia2017`, `schrader2018`, `yuan2014`, `yuan2018`, `lochmanova2019`, `lochmanova2024mcp`, `lochmanova2024plants`, `ryzhaya2026`, `bouyer2011`, `wang2014`, `sequeiraMendes2014`, `lafos2011`, `schubert2006`, `margueronReinberg2011`, `wollmann2012`, `wollmann2017`, `stroud2012`, `jacob2009`, `jacob2014`, `yelagandula2014`, `dealHenikoff2010`, `talbertHenikoff2017`, `bernatavichute2008`, `du2012`, `bourbousse2012`, `sridhar2007`, `cao2008`, `jerzmanowski2007`, `overMichaels2014`, `kotlinski2017`, `harshmanYoungMensch2013`, `xu2005`, `xu2008`, `steger2008`, `wood2018`, `liu2010`, `edmunds2008`, `narita2003`, `adams2007`, `beck2012`, `tian2005`, `tian2012`, `shogrenKnaak2006`, `ay2014`, `brusslan2012`, `brusslan2015`, `buchananWollaston2003`, `buchananWollaston2005`, `boyes2001`, `klepikova2016`, `roudier2011`, `borg2020`, `lang2012`, `rohart2017`, `wilkinson2016`.

### Acción recomendada (OLA 7 o 8)

Substituir patrones del tipo `(Aitchison, 1986)` y `(Pawlowsky-Glahn et al., 2015)` por `[@aitchison1986]` y `[@pawlowsky2015]`. La migración es mecánica una vez consolidado el .bib y permitirá generar la bibliografía formal por Pandoc/Quarto sin la lista APA manual de las líneas 365-426 de `cap4.qmd`.

## 4. Citas con DOI no verificable (`% TODO: DOI`)

Marcadas explícitamente en `references.bib`:

- `ryzhaya2026` — JXB usa patrón `eraXXX`; `erag100` propuesto en versiones previas no resuelve en CrossRef. Cita conservada por referencia metodológica explícita en §4.10.4, §4.11.3 y `_v1`.
- `schrader2018` — DOI ACS plausible (`10.1021/acs.analchem.7b04432`) pero sin confirmación cruzada PubMed; mantener TODO hasta validar con repositorio CEITEC.
- `tian2012` — existen varios trabajos "Tian 2012" sobre top-down de histonas; DOI propuesto provisional `10.1007/978-1-61779-764-4_12` requiere confirmación contra la cita real del §4.0 del master.
- `xu2005` — la cita "Xu et al. 2005" en §4.7.2 sobre K56ac y nucleosoma inestable podría corresponder al trabajo de Xu, Zhang, Zhang 2005 (Mol Cell) en lugar del Xu/Carpenter/Coen propuesto; revisar.
- `lang2012` — el glosario master cita "Lang et al. 2012" como referencia primaria de H2A.X; la entrada propuesta es Lang-Mladek 2012 (Physiologia Plantarum). Alternativa Lang-Mladek 2010 sobre memoria epigenética UV-B.

## 5. Autocitas Pelayo/Valledor/Fraga

- **Pelayo:** `gonzalezDeLena2026` incorporada como `@misc` (revisión PRISMA EpiProfile, depósito local `D:/Antigravity/review_EpiProfile_PRISMA`). Hereda del repositorio `paper_EpiProfile_PLANTS/refs/paper_refs.bib`.
- **Valledor / Fraga:** búsqueda exhaustiva en `D:/Antigravity/**/*.bib` (paper_refs, refs_curated_prisma_v1/v2, openalex_raw, pubmed_raw, repos individuales). **No se han encontrado entradas del grupo sobre proteómica vegetal o epigenética**. Nota dejada en el .bib (líneas finales) para resolución directa con la dirección de tesis.

## 6. Eliminaciones efectivas

Ninguna en esta ola (Pearson 1897 sí se cita; Tukey 1949 y Sandve 2013 quedan como **candidatas a eliminar**, decisión diferida).

## 7. Verificación numérica

```
grep -c '^@' D:/CAP4_NUEVO_OUTPUT/references.bib
84
```

≥65 entradas: **cumplido**. Formato BibTeX preservado (`@article`, `@book`, `@misc`, mismo estilo de campos del archivo original).
