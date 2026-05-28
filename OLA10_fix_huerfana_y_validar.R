# OLA 10 (cierre) — Actualiza phenodata_v4.csv con las 2 huérfanas decididas
#
# Huérfanas decididas (Pelayo + QA objetivo):
#   sample_index 6  (biorep 15, FLOR batch B) — 81 % ceros en QA previo
#   sample_index 28 (biorep 3,  SEN  batch A) — 9,4× menos intensidad que mediana SEN
#
# Validación: tras excluir las 2, el cuadre debe ser exacto con phenodata oficial:
#   YNG A: 5 | BOT A: 5 | BOT B: 6 | FLOR A: 2 | FLOR B: 6 | SEN A: 1 | SEN B: 7 = 32

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
})

OUTDIR <- "D:/AT_virgen/histone_long_table"

ph_v4 <- read_csv(file.path(OUTDIR, "phenodata_v4.csv"),
                  show_col_types = FALSE)

# Aplicar las 2 huérfanas confirmadas
ph_v4_final <- ph_v4 |>
  mutate(
    include_v4 = case_when(
      sample_index == 6  ~ "No",
      sample_index == 28 ~ "No",
      TRUE               ~ "Yes"
    ),
    notes = case_when(
      sample_index == 6 ~
        "Huerfana_tecnica: biorep 15, 81pc ceros en QA, FLOR B excluida",
      sample_index == 28 ~
        "Huerfana_tecnica: biorep 3, 53.6pc ceros + 9.4x menos area que mediana SEN, SEN A excluida",
      TRUE ~ ""
    )
  )

write_csv(ph_v4_final, file.path(OUTDIR, "phenodata_v4.csv"))

# Validar cuadre
included <- ph_v4_final |> filter(include_v4 == "Yes")
cat("== Phenodata v4 FINAL ==\n")
cat("Total filas:           ", nrow(ph_v4_final), "\n")
cat("Incluidas (include=Yes):", nrow(included), "\n")
cat("Excluidas (include=No): ", sum(ph_v4_final$include_v4 == "No"), "\n\n")

cat("== Distribución por grupo × batch (incluidas) ==\n")
final_counts <- included |>
  count(group_real, batch, name = "n_included") |>
  arrange(group_real, batch)
print(as.data.frame(final_counts))

# Cuadre vs phenodata oficial
ph_oficial <- read_tsv(file.path(OUTDIR, "phenodata_v4_oficial.tsv"),
                       show_col_types = FALSE)
oficial_counts <- ph_oficial |>
  count(Sample_Group, Batch, name = "n_oficial") |>
  rename(group_real = Sample_Group, batch = Batch)

check <- full_join(final_counts, oficial_counts,
                   by = c("group_real", "batch")) |>
  mutate(diff = n_included - n_oficial)

cat("\n== Cuadre vs phenodata oficial ==\n")
print(as.data.frame(check))
if (all(check$diff == 0)) {
  cat("\n[OK] CUADRA PERFECTAMENTE: 32 muestras en ambos lados.\n")
} else {
  cat("\n[FAIL] Hay discrepancias.\n")
}

cat("\n== Lista final de muestras incluidas (n=32) ==\n")
print(as.data.frame(included |>
                      select(sample_index, sample_name_tsv, biorep_id,
                             group_real, batch)))
