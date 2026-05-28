# OLA 10 — Cruce CSV maestro x phenodata real
#
# Detecta inconsistencias entre los sample_ids del cargador v3.2.0
# y el phenodata real del experimento (lote 2025017).
# Objetivo: descubrir si "YNG" del pipeline es realmente 10H+14H y
# documentar el batch_effect por Date.

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(stringr)
  library(tidyr)
})

OUTDIR <- "D:/AT_virgen/histone_long_table"

# 1) phenodata real --------------------------------------------------------
ph <- read_tsv(file.path(OUTDIR, "phenodata.tsv"),
               show_col_types = FALSE,
               col_types = cols(.default = col_character()))

cat("== Phenodata estructura ==\n")
cat("filas:", nrow(ph), "\n")
cat("cols:", paste(names(ph), collapse = ", "), "\n\n")

# Extraer sample_index del Sample_Name (la parte antes de la coma)
ph <- ph |>
  mutate(
    sample_index = as.integer(str_extract(Sample_Name, "^[0-9]+")),
    biorep_id    = str_extract(Sample_Name, "[^-]+$"),
    date_acq     = Date
  )

cat("== Distribución de grupos (phenodata real) ==\n")
print(table(ph$Sample_Group))

cat("\n== Distribución por fecha de adquisición ==\n")
print(table(ph$Date))

cat("\n== Cross-tab grupo x fecha ==\n")
print(table(ph$Sample_Group, ph$Date))

# 2) CSV maestro (cargador v3.2.0) ----------------------------------------
long <- read_csv(file.path(OUTDIR, "histone_ratios_long.csv"),
                 show_col_types = FALSE)

samples_pipeline <- long |>
  distinct(sample_index, sample_name, sample_code, sample_group) |>
  arrange(sample_index)

cat("\n== Pipeline cargador v3.2.0 ==\n")
cat("muestras únicas:", nrow(samples_pipeline), "\n")
print(table(samples_pipeline$sample_group))

# 3) Cruce --------------------------------------------------------------
cruce <- samples_pipeline |>
  left_join(
    ph |> select(sample_index, Sample_Name_pheno = Sample_Name,
                 Sample_Group_pheno = Sample_Group,
                 Code_pheno = Code, Date_pheno = Date,
                 Processing_order),
    by = "sample_index"
  )

cat("\n== Mapping sample_index → grupo pipeline vs phenodata ==\n")
print(cruce |>
        select(sample_index, sample_name, sample_group,
               Sample_Group_pheno, Code_pheno, Date_pheno) |>
        as.data.frame())

# 4) Detectar inconsistencias ------------------------------------------
cat("\n== Inconsistencias ==\n")

# 4a) ¿hay sample_index en pipeline que falten en phenodata?
in_pipeline_not_pheno <- cruce |> filter(is.na(Sample_Group_pheno))
cat("Pipeline solo (no en phenodata):", nrow(in_pipeline_not_pheno), "\n")
if (nrow(in_pipeline_not_pheno) > 0) {
  print(in_pipeline_not_pheno |> select(sample_index, sample_name))
}

# 4b) ¿hay sample_index en phenodata que falten en pipeline?
in_pheno_not_pipeline <- ph |>
  anti_join(samples_pipeline, by = "sample_index")
cat("\nPhenodata solo (no en pipeline):", nrow(in_pheno_not_pipeline), "\n")
if (nrow(in_pheno_not_pipeline) > 0) {
  print(in_pheno_not_pipeline |> select(sample_index, Sample_Name,
                                         Sample_Group, Code))
}

# 4c) ¿discrepancia de grupo?
group_mismatch <- cruce |>
  filter(!is.na(Sample_Group_pheno),
         sample_group != Sample_Group_pheno) |>
  select(sample_index, sample_name, sample_group, Sample_Group_pheno)

cat("\nDiscrepancia de grupo pipeline vs phenodata:\n")
print(as.data.frame(group_mismatch))

# 4d) Si YNG = 10H+14H, validar
if (nrow(group_mismatch) > 0) {
  yng_real <- group_mismatch |>
    filter(sample_group == "YNG") |>
    pull(Sample_Group_pheno) |>
    table()
  cat("\nSi YNG del pipeline se descompone:\n")
  print(yng_real)
}

# 5) Persistir mapping reconciliado ------------------------------------
mapping_reconciled <- cruce |>
  mutate(
    # Grupo real corregido
    group_real = coalesce(Sample_Group_pheno, sample_group),
    # Batch técnico = fecha de adquisición
    batch_date = Date_pheno
  ) |>
  select(sample_index, sample_name, sample_code, sample_group,
         group_real, batch_date, Processing_order, Code_pheno)

write_csv(mapping_reconciled,
          file.path(OUTDIR, "OLA10_sample_mapping_reconciled.csv"))

cat("\n[OK] Mapping reconciliado escrito en:\n")
cat("    ", file.path(OUTDIR, "OLA10_sample_mapping_reconciled.csv"), "\n")

cat("\n=== Resumen ===\n")
cat("Pipeline grupos:", paste(sort(unique(samples_pipeline$sample_group)), collapse=", "), "\n")
cat("Phenodata grupos:", paste(sort(unique(ph$Sample_Group)), collapse=", "), "\n")
cat("Total muestras pipeline:", nrow(samples_pipeline), "\n")
cat("Total muestras phenodata:", nrow(ph), "\n")
cat("Fechas batch:", paste(sort(unique(ph$Date)), collapse=", "), "\n")
