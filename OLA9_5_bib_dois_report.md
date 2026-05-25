# OLA 9.5 · Bibliografía, DOIs y migración APA → @key

Fecha: 2026-05-25. Riesgo mínimo, verificación CrossRef + Oxford Academic + ACS.

## DOIs verificados (5 de 5)

| Clave | Resultado | Acción aplicada |
|---|---|---|
| `ryzhaya2026` | DOI `10.1093/jxb/erag100` **canónico** (Oxford Academic, advance article 2026). El sufijo `erag` corresponde a la nueva serie 2026, no a error tipográfico. | TODO eliminado; DOI conservado; nota explicativa añadida. |
| `schrader2018` | DOI original `7b04432` devuelve 404. La referencia metodológica correcta es Schräder, Ziemianowicz, Merx & Schriemer 2018, *Anal Chem* 90(5):3083-3090, DOI `10.1021/acs.analchem.7b03948`. | Autores, título, número e issue corregidos; DOI sustituido; TODO eliminado. |
| `tian2012` | DOI `10.1007/978-1-61779-764-4_12` corresponde a un capítulo de *tissue engineering*, no a histonas. La referencia real es Tian Z et al. 2012, *Genome Biology* 13:R86, DOI `10.1186/gb-2012-13-10-r86`. | Entrada reescrita con 10 autores reales, journal y DOI canónicos; TODO eliminado. |
| `xu2005` | La entrada anterior (Xu, Carpenter, Coen 2005 *Genetics* sobre ASH1) **no existe** en CrossRef ni Genetics; el DOI da 404. La referencia correcta para K56ac y nucleosoma inestable es Xu F, Zhang K & Grunstein M 2005, *Cell* 121(3):375-385, DOI `10.1016/j.cell.2005.03.011`. | Entrada reescrita por completo; TODO eliminado. |
| `lang2012` | DOI `10.1111/j.1399-3054.2011.01561.x` (Lang-Mladek et al. 2012 *Physiologia Plantarum* sobre UV-B/ARIADNE12) **verificado en CrossRef**. | TODO sustituido por nota constructiva sugiriendo Lang-Mladek 2010 *Mol Plant* como complemento si la cita en cap. 3 alude a H2A.X canónico. |

## Huérfanas

Búsqueda en `cap4.qmd` (activo) y en todos los `.qmd` de `reports/`:

- `tukey1949`: 0 citas en qmd activo. **Eliminada del .bib**.
- `sandve2013`: 0 citas en qmd activo. **Eliminada del .bib**.

Las cinco entradas con TODO (Ryzhaya, Schrader, Tian, Xu, Lang) tampoco se citan aún en `cap4.qmd` v3.1.0 (estaban planificadas para cap. 3 reescritura). Se conservan con DOIs corregidos para uso futuro.

## Migración APA → `[@key]` en cap4.qmd

22 patrones APA únicos migrados con `Edit` (varios con múltiples ocurrencias, conteo bruto post-migración: 28 instancias `[@`). Conjunto seguro, sin reflexión ambigua:

- Aitchison 1986, Pawlowsky-Glahn 2015, Egozcue 2003, Palarea-Albaladejo 2015 (CoDA core).
- Welch 1947, Benjamini-Hochberg 1995, Delacre 2017, Cumming 2014 (inferencia/efecto).
- Ignatiadis 2016, Tibshirani 2001, Suzuki 2006 (IHW/clustering).
- Garcia 2007, Sidoli 2016 (proteómica histonas).
- Stroud 2012, Wollmann 2017 (variantes H3).
- Bouyer 2011, Wang 2014, Sequeira-Mendes 2014, Ay 2014, Brusslan 2015, Jacob 2014, Lafos 2011, Beck 2012, Bernatavichute 2008, Du 2012, Pearson 1897.

## Pendientes para v3.2.0+

- Narrativas tipo "Aitchison (1986)" o "Martín-Fernández et al. (2015)" no migradas: requieren la forma `@key [yyyy]` de pandoc-citeproc, que altera la lectura y conviene revisar en bloque con un pase manual o regex dirigida.
- Citas dentro de figuras/tablas (no parseadas aquí).
- Cuando se reescriba cap. 3 y se introduzcan ryzhaya2026, schrader2018, tian2012, xu2005, lang2012, los DOIs ya son canónicos y reusables sin más verificación.
