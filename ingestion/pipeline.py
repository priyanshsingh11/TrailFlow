import os

from ingestion.loader import load_excel
from ingestion.domain_mapper import map_domain
from ingestion.cleaner import clean_dataframe
from ingestion.config import DOMAIN_CONFIG


def run_pipeline(raw_dir: str, output_dir: str):
    """
    Runs the full ingestion + cleaning pipeline
    for all studies and files.
    """

    os.makedirs(output_dir, exist_ok=True)

    for study_id in os.listdir(raw_dir):
        study_path = os.path.join(raw_dir, study_id)

        # Skip non-study folders
        if not os.path.isdir(study_path):
            continue

        print(f"\nProcessing study: {study_id}")

        for file in os.listdir(study_path):
            if not file.endswith(".xlsx"):
                continue

            file_path = os.path.join(study_path, file)

            print(f"  Loading file: {file}")

            # 1. Load raw data
            df = load_excel(file_path)

            # 🔑 VERY IMPORTANT: skip empty / unusable files
            if df is None:
                print(f"  Skipping file (no usable data): {file}")
                continue

            # 2. Map domain
            domain = map_domain(file, DOMAIN_CONFIG)

            # 3. Clean data
            cleaned_df = clean_dataframe(
                df=df,
                study_id=study_id,
                domain=domain,
                source_file=file
            )

            # 4. Save cleaned output
            output_filename = f"{study_id}_{domain}_{file.replace('.xlsx', '.csv')}"
            output_path = os.path.join(output_dir, output_filename)

            cleaned_df.to_csv(output_path, index=False)

            print(f"  Saved cleaned file → {output_filename}")
