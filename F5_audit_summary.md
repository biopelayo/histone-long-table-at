# F5 · Auditoría paralela de 28 scripts R (4 sub-agentes)

**Veredicto global:** APTO para `tar_make()` sin parches. 4 WARNINGS no bloqueantes documentadas para F8.

## Bloque QC+Filtrado (03-06h) — 13 scripts

Todos OK. Las constantes hardcoded (25 violaciones compositional, 6 muestras con >40 % ceros, n=33 post-exclusión, n_per_group={5,11,9,9}) **siguen siendo válidas** porque F1 demostró igualdad numérica byte-a-byte. `SAMPLES_TO_EXCLUDE = "6,2025017_15_AT_FLOR"` casa exactamente con la muestra del 81 % ceros que detecté en el QA del wrangler.

## Bloque CoDA+EDA (07-11) — 7 scripts

Todos OK. CLR/ILR son intrínsecamente per-péptido, indiferentes al diseño. `cmultRepl` GBM opera fila a fila tras D-024 (filtro nonzero por grupo), así que YNG=5 no rompe el prior. `stage_palette` casa con CONDITION_LEVELS = {YNG, BOT, FLOR, SEN}.

## Bloque Stats (12-14b + 23) — 8 scripts

Todos OK con 2 WARNINGS:
- **W1 (13c)** Bootstrap percentil para Hedges g IC95 %; Cumming 2014 lo acepta para n moderado pero BCa sería preferible con YNG=5. No bloqueante.
- **W2 (23)** IHW con covariable `abs(log2fc)` no independiente del p-valor bajo Welch. Ignatiadis 2016 §3.2 advierte. Documentar como exploratorio.

## Bloque PTMs+Viz+Report (15-22, 99) — 11 scripts

Todos OK con 2 WARNINGS:
- **W3 (18)** Umbral fijo `rho_min=0.7` para correlation networks puede inflar redes YNG (n=5, solo 120 permutaciones posibles). Documentar.
- **W4 (21)** sPLS-DA reemplaza NA/Inf por 0; debería abortar si la matriz CLR upstream trae NA (indicaría bug). Cambio defensivo.

## Patches sugeridos (NO aplicados — pendientes para v3.0.1 o F8)

1. **18_correlation_networks.R**: `rho_min` adaptativo (`if n<6 then 0.85 else 0.7`).
2. **21_plsda.R**: cambiar imputación silenciosa por log_warn + abort si NA en CLR.
3. **13c_bootstrap_hedges_ci.R**: migrar a `boot::boot.ci(type="bca")` para n pequeños.
4. **23_ihw_alternative.R**: cambiar covariable a `n_a + n_b` o CV intra-grupo; reportar como secundario.

## Sistema Visual Pelamovic — verificado

- Botanical Green `#2D6A4F` presente
- Stage palette Okabe-Ito: YNG `#56B4E9`, BOT `#E69F00`, FLOR `#CC79A7`, SEN `#D55E00`
- Exportación dual PNG 300 DPI + cairo_pdf via `save_fig`
- Cumplido en 16, 17, 18, 18b, 19, 20

## Cardinalidad final esperada (sin sorpresas)

- Pre-filtrado: 9010 filas, 34 muestras, 265 peptidoformas
- Post-04 (exclusión muestras): 33 muestras
- Post-06h (D-024 filtro nonzero por grupo): ~97 peptidoformas (igual que v2.0.0)
- Stats: 6 contrastes pareados con BH-FDR por contraste
- Hits esperados: 4 BH-FDR<0.05 en BOT-SEN (replicable porque valores idénticos)
