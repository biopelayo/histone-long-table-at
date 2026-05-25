# Diff Report · dataset viejo vs nueva tabla maestra

**Fecha:** 2026-05-24  
**Viejo:** `D:\CAP4_NUEVO_INPUT\histone_ratios.txt`  
**Nuevo (long):** `D:\AT_virgen\histone_long_table\histone_ratios_long.csv`

## 1. Muestras

- Viejo: **34** muestras únicas
- Nuevo: **34** muestras únicas
- Comunes: **34**
- Solo en viejo: **0** → []
- Solo en nuevo: **0** → []

## 2. Peptidoformas

- Viejo: **265** únicas
- Nuevo: **265** únicas
- Comunes: **265**
- Solo en viejo: **0**
- Solo en nuevo: **0**

## 3. Valores (ratios) en celdas comunes (peptidoforma × muestra)

- Celdas comparadas: **9010**
- Idénticas (|Δ|<1e-6): **9010** (100.0 %)
- Pequeñas (1e-6≤|Δ|<1e-3): **0** (0.0 %)
- Grandes (|Δ|≥1e-3): **0** (0.0 %)
- Peptidoformas con alguna discrepancia: **0** de 265

### Top 20 discrepancias por |Δ| absoluta

| peptidoform | sample | ratio_old | ratio_new | |Δ| | rel_diff |
|---|---|---:|---:|---:|---:|
| `H3_3_8 unmod` | 2025017_10_AT_YNG | 0.6672 | 0.6672 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_11_AT_YNG | 0.8100 | 0.8100 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_12_AT_FLOR | 0.6266 | 0.6266 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_13_AT_YNG | 0.6059 | 0.6059 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_14_AT_FLOR | 0.5593 | 0.5593 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_15_AT_FLOR | 0.4525 | 0.4525 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_16_AT_FLOR | 0.6250 | 0.6250 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_17_AT_SEN | 0.5713 | 0.5713 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_18_AT_FLOR | 0.5813 | 0.5813 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_19_AT_SEN | 0.5665 | 0.5665 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_1_AT_YNG | 0.6485 | 0.6485 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_20_AT_FLOR | 0.5724 | 0.5724 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_21_AT_BOT | 0.5707 | 0.5707 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_22_AT_BOT | 0.5804 | 0.5804 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_23_AT_SEN | 0.5811 | 0.5811 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_24_AT_FLOR | 0.6145 | 0.6145 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_25_AT_BOT | 0.6079 | 0.6079 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_26_AT_SEN | 0.5556 | 0.5556 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_27_AT_SEN | 0.6151 | 0.6151 | 0.0000 | 0.0000 |
| `H3_3_8 unmod` | 2025017_28_AT_BOT | 0.5778 | 0.5778 | 0.0000 | 0.0000 |

## 4. Veredicto

**Identidad perfecta** en celdas comunes. La diferencia entre ficheros es solo de cobertura (más samples y peptidoformas en el nuevo).

- Muestra(s) extra en el nuevo: **[]**
- Peptidoformas extra en el nuevo: **0**

**Recomendación operativa:** la nueva tabla es la fuente correcta para v3.0.0. El input v2.0.0 queda como histórico.