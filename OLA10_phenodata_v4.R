# OLA 10 v4 — Construye phenodata_v4.csv canónico
#
# Toma:
#   - el phenodata oficial del usuario (32 muestras, YNG/SEN/BOT/FLOR, batch A/B)
#   - los 34 sample_index del TSV crudo (cargador v3.2.0)
# Genera:
#   - phenodata_v4.csv con 34 filas, una por sample_index
#   - column include_v4 (Yes/No) según si la muestra está en el phenodata oficial
#   - column phenodata_code (Sample_Name del phenodata si match, NA si huérfana)
#
# Hipótesis de asignación de batch:
#   biorep_id (del nombre TSV) ≤ 14 → batch A (20250506)
#   biorep_id ≥ 15 → batch B (20250507)

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(stringr)
  library(tidyr)
})

OUTDIR <- "D:/AT_virgen/histone_long_table"

# 1) phenodata oficial -----------------------------------------------------
ph <- read_tsv(file.path(OUTDIR, "phenodata_v4_oficial.tsv"),
               show_col_types = FALSE,
               col_types = cols(.default = col_character()))

cat("== Phenodata oficial v4 ==\n")
cat("filas:", nrow(ph), "\n")
cat("grupos:\n"); print(table(ph$Sample_Group, ph$Batch))
cat("\n")

# 2) TSV crudo: extraer sample_index, biorep, etiqueta TSV ----------------
long <- read_csv(file.path(OUTDIR, "histone_ratios_long.csv"),
                 show_col_types = FALSE)

samples_tsv <- long |>
  distinct(sample_index, sample_name, sample_code, sample_group) |>
  arrange(sample_index) |>
  mutate(
    biorep_id = as.integer(sample_code),
    tsv_label = sample_group,
    batch_hyp = ifelse(biorep_id <= 14, "A", "B"),
    date_hyp  = ifelse(biorep_id <= 14, "20250506", "20250507")
  )

cat("== TSV crudo (34 samples) ==\n")
cat("grupos x batch hipotetico:\n")
print(table(samples_tsv$tsv_label, samples_tsv$batch_hyp))
cat("\n")

# 3) Validar cuadre ------------------------------------------------------
tsv_counts <- samples_tsv |>
  count(tsv_label, batch_hyp, name = "n_tsv") |>
  rename(Sample_Group = tsv_label, Batch = batch_hyp)

ph_counts <- ph |>
  count(Sample_Group, Batch, name = "n_pheno")

merged_counts <- full_join(tsv_counts, ph_counts,
                           by = c("Sample_Group", "Batch")) |>
  mutate(
    n_tsv = coalesce(n_tsv, 0L),
    n_pheno = coalesce(n_pheno, 0L),
    diff = n_tsv - n_pheno
  )

cat("== Cuadre de conteos TSV vs phenodata ==\n")
print(as.data.frame(merged_counts))
cat("\n")

# 4) Identificar huérfanas -----------------------------------------------
# Las huérfanas son las muestras del TSV donde la celda (grupo, batch) tiene
# más TSV que phenodata. Su identidad concreta requiere decisión humana
# (Pelayo confirmará por biorep_id).
cat("== Posibles huérfanas (grupo,batch con n_tsv > n_pheno) ==\n")
huerfanas_celdas <- merged_counts |>
  filter(diff > 0)
print(as.data.frame(huerfanas_celdas))
cat("\n")

# Listar candidatas concretas
for (i in seq_len(nrow(huerfanas_celdas))) {
  g <- huerfanas_celdas$Sample_Group[i]
  b <- huerfanas_celdas$Batch[i]
  d <- huerfanas_celdas$diff[i]
  cands <- samples_tsv |>
    filter(tsv_label == g, batch_hyp == b) |>
    arrange(biorep_id)
  cat(sprintf("\nCandidatas %s batch %s (descartar %d):\n", g, b, d))
  print(as.data.frame(cands |> select(sample_index, sample_name, biorep_id)))
}

# 5) Generar phenodata_v4.csv inicial ------------------------------------
# Sin asignar Code/processing_order todavía (necesita mapeo biorep -> Code).
# Solo se incluye group_real (= tsv_label, ya validado) + batch_hyp.

phenodata_v4 <- samples_tsv |>
  transmute(
    sample_index,
    sample_name_tsv = sample_name,
    biorep_id,
    group_real      = tsv_label,
    batch           = batch_hyp,
    date            = date_hyp,
    include_v4      = "Yes",  # por defecto incluida, ajustar abajo
    notes           = ""
  )

# Marcar huérfanas técnicas según mi hipótesis (Pelayo confirmará):
#   - biorep 15 (sample_index 6, FLOR batch B según hipótesis): tenía 81 % ceros
#     en QA previo → fallida técnica conocida
#   - 1 huérfana SEN batch A (biorep 2 o 3): Pelayo elige cuál
phenodata_v4 <- phenodata_v4 |>
  mutate(
    include_v4 = case_when(
      biorep_id == 15 & group_real == "FLOR" ~ "No",  # 81% ceros previo
      TRUE ~ include_v4
    ),
    notes = case_when(
      biorep_id == 15 & group_real == "FLOR" ~
        "Huerfana_tecnica_81pc_ceros_QA",
      TRUE ~ notes
    )
  )

# 6) Persistir -----------------------------------------------------------
write_csv(phenodata_v4, file.path(OUTDIR, "phenodata_v4.csv"))

cat("\n== Phenodata v4 generado ==\n")
print(as.data.frame(phenodata_v4))

cat("\n[OK] Escrito:", file.path(OUTDIR, "phenodata_v4.csv"), "\n")

# 7) Resumen final --------------------------------------------------------
cat("\n=== RESUMEN ===\n")
cat("Total samples TSV:        ", nrow(samples_tsv), "\n")
cat("Total samples phenodata:  ", nrow(ph), "\n")
cat("Total include_v4 = Yes:   ", sum(phenodata_v4$include_v4 == "Yes"), "\n")
cat("Total include_v4 = No:    ", sum(phenodata_v4$include_v4 == "No"), "\n")
cat("Pendiente Pelayo: 1 huerfana SEN batch A (biorep 2 o 3) o 1 FLOR batch B distinta a biorep 15.\n")
