from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil

from services.analysis_service import run_full_analysis

app = FastAPI(title="TrailFlow API")

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = RAW_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File uploaded successfully", "file": file.filename}


@app.post("/run-analysis")
def run_analysis():
    result = run_full_analysis(
        raw_dir=str(RAW_DIR),
        processed_dir=PROCESSED_DIR
    )
    return result
