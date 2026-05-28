# OLA 10b — Decidir cuál SEN batch A es la huérfana
#
# Candidatas:
#   biorep 2 → sample_index 22, nombre TSV "2025017_2_AT_SEN"
#   biorep 3 → sample_index 28, nombre TSV "2025017_3_AT_SEN"
#
# Criterios de decisión (la peor en QA = huérfana técnica):
#   1. fracción de ceros en ratios (peor = mayor)
#   2. desviación de la suma compositional
#   3. desviación de RT mediano vs el resto del grupo SEN
#   4. correlación CLR-rank vs perfil mediano SEN

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(stringr)
})

OUTDIR <- "D:/AT_virgen/histone_long_table"

long <- read_csv(file.path(OUTDIR, "histone_ratios_long.csv"),
                 show_col_types = FALSE)

# Identificar SEN batch A según hipótesis biorep ≤ 14
sen_a <- long |>
  filter(sample_group == "SEN",
         as.integer(sample_code) <= 14)

candidatas <- sort(unique(sen_a$sample_index))
cat("== Candidatas SEN batch A (biorep ≤ 14) ==\n")
print(sen_a |> distinct(sample_index, sample_name, sample_code))

# Y el resto SEN como referencia
sen_resto <- long |>
  filter(sample_group == "SEN",
         !sample_index %in% candidatas)

cat("\n== Resto SEN (referencia) ==\n")
print(sen_resto |> distinct(sample_index, sample_name) |> head(3))
cat("...\n")
cat("Total resto SEN:", n_distinct(sen_resto$sample_index), "muestras\n\n")

# 1) Fracción de ceros por candidata ------------------------------------
zeros_per_sample <- long |>
  group_by(sample_index, sample_name) |>
  summarise(
    n_total = n(),
    n_zero  = sum(ratio == 0, na.rm = TRUE),
    frac_zero = n_zero / n_total,
    .groups = "drop"
  )

cat("== 1) Fracción de ceros ==\n")
print(zeros_per_sample |>
        filter(sample_index %in% candidatas))
cat("Mediana SEN resto:", median(zeros_per_sample$frac_zero[
  zeros_per_sample$sample_index %in% unique(sen_resto$sample_index)]), "\n")
cat("Mediana global:    ", median(zeros_per_sample$frac_zero), "\n\n")

# 2) Suma compositional por péptido (debe ~1 por (peptide, sample)) ------
sums_per <- long |>
  group_by(sample_index, sample_name, peptide) |>
  summarise(sum_ratios = sum(ratio, na.rm = TRUE), .groups = "drop") |>
  mutate(deviation = abs(sum_ratios - 1))

dev_per_sample <- sums_per |>
  group_by(sample_index, sample_name) |>
  summarise(
    mean_dev = mean(deviation, na.rm = TRUE),
    max_dev  = max(deviation, na.rm = TRUE),
    n_violations = sum(deviation > 0.05, na.rm = TRUE),
    .groups = "drop"
  )

cat("== 2) Desviación compositional ==\n")
print(dev_per_sample |>
        filter(sample_index %in% candidatas))
cat("Mediana mean_dev SEN resto:", median(dev_per_sample$mean_dev[
  dev_per_sample$sample_index %in% unique(sen_resto$sample_index)]), "\n\n")

# 3) Perfil correlación rank vs mediana SEN ------------------------------
sen_ref_profile <- sen_resto |>
  group_by(peptidoform) |>
  summarise(ratio_median = median(ratio, na.rm = TRUE), .groups = "drop")

cor_to_median <- candidatas |>
  purrr::map_dfr(function(si) {
    sub <- long |>
      filter(sample_index == si) |>
      left_join(sen_ref_profile, by = "peptidoform")
    tibble(
      sample_index = si,
      n_obs        = nrow(sub),
      spearman_to_SEN_median = cor(sub$ratio, sub$ratio_median,
                                    method = "spearman",
                                    use = "pairwise.complete.obs")
    )
  })

cat("== 3) Spearman con perfil mediano SEN (1 = perfecto, 0 = sin estructura) ==\n")
print(cor_to_median)
cat("\n")

# 4) Suma total de areas (proxy de injection success) -------------------
area_per_sample <- long |>
  group_by(sample_index, sample_name) |>
  summarise(total_area = sum(area, na.rm = TRUE), .groups = "drop")

cat("== 4) Suma total de areas (proxy intensity) ==\n")
print(area_per_sample |>
        filter(sample_index %in% candidatas))
cat("Mediana total_area SEN resto:", median(area_per_sample$total_area[
  area_per_sample$sample_index %in% unique(sen_resto$sample_index)]), "\n\n")

# 5) Veredicto -----------------------------------------------------------
cat("=== VEREDICTO ===\n")
combined <- zeros_per_sample |>
  inner_join(dev_per_sample,   by = c("sample_index", "sample_name")) |>
  inner_join(cor_to_median,    by = "sample_index") |>
  inner_join(area_per_sample,  by = c("sample_index", "sample_name")) |>
  filter(sample_index %in% candidatas) |>
  arrange(desc(frac_zero), desc(mean_dev), spearman_to_SEN_median, total_area)

print(as.data.frame(combined))

cat("\n→ La huérfana SEN batch A más probable es la de la fila 1 (peor en QA).\n")
cat("  Si las métricas son comparables, marcar AMBAS como dudosas\n")
cat("  y mantener phenodata con 33 incluidas (sin descartar ninguna).\n")
