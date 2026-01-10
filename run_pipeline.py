from ingestion.pipeline import run_pipeline

RAW_DIR = "data/raw"
OUTPUT_DIR = "data/processed"

run_pipeline(RAW_DIR, OUTPUT_DIR)
