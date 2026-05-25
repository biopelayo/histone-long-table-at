# OLA 1 — Verdad numérica de las peptidoformas BH-FDR<0.05
#
# Ejecuta desde D:/CAP4_NUEVO_OUTPUT/
# Output: D:/AT_virgen/histone_long_table/T_verdad_4hits.{csv,md}

suppressPackageStartupMessages({
  library(targets)
  library(dplyr)
  library(readr)
  library(tibble)
  library(stringr)
})

OUTDIR <- "D:/AT_virgen/histone_long_table"
dir.create(OUTDIR, showWarnings = FALSE, recursive = TRUE)

# 1A) Forzar invalidación de stats + rerun
cat("== OLA 1A · Invalidando stats targets ==\n")
tryCatch(
  targets::tar_invalidate(any_of(c(
    "stats_anova", "stats_welch_anova",
    "stats_pairwise", "stats_permutation", "stats_hedges_ci",
    "volcano", "volcano_with_effect", "ihw_alternative"
  ))),
  error = function(e) cat("  invalidate warning:", conditionMessage(e), "\n")
)

cat("\n== OLA 1A · tar_make() stats ==\n")
targets::tar_make(
  names = any_of(c("stats_welch_anova", "stats_pairwise",
                   "stats_permutation", "stats_hedges_ci",
                   "ihw_alternative"))
)

# 1B) Leer rds frescos
cat("\n== OLA 1B · Cargando rds frescos ==\n")
proc <- "D:/CAP4_NUEVO_OUTPUT/data/processed"

read_safe <- function(name) {
  f <- file.path(proc, paste0(name, ".rds"))
  if (file.exists(f)) {
    cat("  ✓", name, "\n")
    readRDS(f)
  } else {
    cat("  ✗", name, "(no encontrado)\n")
    NULL
  }
}

# Buscar el rds principal de pairwise (puede tener varios)
pairwise_files <- list.files(proc, pattern = "^13_", full.names = TRUE)
cat("  ficheros 13_*:\n"); cat("   ", basename(pairwise_files), sep = "\n    ")
hedges_files   <- list.files(proc, pattern = "^13c_", full.names = TRUE)
cat("  ficheros 13c_*:\n"); cat("   ", basename(hedges_files), sep = "\n    ")
ihw_files      <- list.files(proc, pattern = "^23_", full.names = TRUE)
cat("  ficheros 23_*:\n"); cat("   ", basename(ihw_files), sep = "\n    ")

# Heurística: tomar el primero que tenga columnas fdr_bh / cohens_d
pick_with_cols <- function(files, required_cols) {
  for (f in files) {
    obj <- tryCatch(readRDS(f), error = function(e) NULL)
    if (is.data.frame(obj) && all(required_cols %in% names(obj))) {
      cat("  >>", basename(f), "tiene", paste(required_cols, collapse=","), "\n")
      return(list(name = basename(f), data = obj))
    }
  }
  NULL
}

pairwise <- pick_with_cols(pairwise_files,
                           c("peptidoform", "contrast", "fdr_bh"))
hedges   <- pick_with_cols(hedges_files,
                           c("peptidoform", "contrast"))

if (is.null(pairwise)) {
  stop("No se encontró rds pairwise con cols peptidoform+contrast+fdr_bh")
}

cat("\nUsando pairwise:", pairwise$name, "(", nrow(pairwise$data), "filas)\n")
if (!is.null(hedges)) {
  cat("Usando hedges:  ", hedges$name, "(", nrow(hedges$data), "filas)\n")
}

# 1C) Extraer hits BH-FDR<0.05
cat("\n== OLA 1C · Filtrando BH-FDR<0.05 ==\n")
hits <- pairwise$data %>%
  filter(!is.na(fdr_bh), fdr_bh < 0.05) %>%
  arrange(fdr_bh)
cat("  hits BH-FDR<0.05:", nrow(hits), "\n")

if (nrow(hits) > 0) {
  cat("\n  resumen por contraste:\n")
  print(hits %>% count(contrast))
}

# Enriquecer con Hedges g + IC95% si disponible
if (!is.null(hedges) && nrow(hits) > 0) {
  hits_enriched <- hits %>%
    left_join(
      hedges$data %>% select(any_of(c(
        "peptidoform", "contrast", "hedges_g", "g", "cohens_d",
        "ci_lo", "ci_hi", "ci_lower", "ci_upper",
        "lower", "upper"
      ))),
      by = c("peptidoform", "contrast")
    )
} else {
  hits_enriched <- hits
}

cat("\n  columnas finales:", paste(names(hits_enriched), collapse = ", "), "\n")

# 1D) Persistir
write_csv(hits_enriched, file.path(OUTDIR, "T_verdad_4hits.csv"))
cat("\n[OK] CSV escrito:", file.path(OUTDIR, "T_verdad_4hits.csv"), "\n")

# Generar MD
md_lines <- c(
  "# Verdad numérica · 4 peptidoformas BH-FDR<0.05",
  "",
  "**Fecha:** 2026-05-25",
  paste0("**Fuente:** `", pairwise$name, "` (post-tar_make v3.0.0)"),
  paste0("**Hedges:** `", if (!is.null(hedges)) hedges$name else "n/a", "`"),
  "",
  "## Tabla canónica",
  ""
)

# Tabla markdown
if (nrow(hits_enriched) > 0) {
  # Headers
  cols_show <- intersect(
    c("contrast", "peptidoform", "peptide",
      "fdr_bh", "p_value", "log2fc",
      "hedges_g", "g", "cohens_d",
      "ci_lo", "ci_hi", "ci_lower", "ci_upper"),
    names(hits_enriched)
  )
  hdr <- paste0("| ", paste(cols_show, collapse = " | "), " |")
  sep <- paste0("|", paste(rep("---", length(cols_show)), collapse = "|"), "|")
  md_lines <- c(md_lines, hdr, sep)
  for (i in seq_len(nrow(hits_enriched))) {
    vals <- vapply(cols_show, function(c) {
      v <- hits_enriched[[c]][i]
      if (is.numeric(v)) formatC(v, format = "g", digits = 4) else as.character(v)
    }, character(1))
    md_lines <- c(md_lines, paste0("| ", paste(vals, collapse = " | "), " |"))
  }
} else {
  md_lines <- c(md_lines, "**Sin hits BH-FDR<0.05 detectados.**")
}

md_lines <- c(md_lines, "",
  "## Resumen por contraste",
  "",
  paste(capture.output(print(hits_enriched %>% count(contrast))), collapse = "\n"),
  "",
  "## Decisión D-034 (propuesta)",
  "",
  "Las 4 peptidoformas listadas son la **verdad canónica** para cap. 4 v3.1.0.",
  "Cualquier prosa downstream debe usar exactamente esta tabla."
)

writeLines(md_lines, file.path(OUTDIR, "T_verdad_4hits.md"))
cat("[OK] MD escrito:", file.path(OUTDIR, "T_verdad_4hits.md"), "\n")

cat("\n=== OLA 1 COMPLETADA ===\n")
