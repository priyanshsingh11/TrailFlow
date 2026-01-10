import pandas as pd
import numpy as np
from datetime import datetime


# Values commonly used to represent missing data
MISSING_VALUES = ["", "NA", "N/A", "NULL", "null", "na"]


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Make column names consistent and machine-friendly.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )
    return df


def normalize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert common missing value markers to NaN.
    """
    return df.replace(MISSING_VALUES, np.nan)


def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows where all values are missing.
    """
    return df.dropna(how="all")


def add_metadata(
    df: pd.DataFrame,
    study_id: str,
    domain: str,
    source_file: str
) -> pd.DataFrame:
    """
    Add standard metadata columns.
    """
    df["study_id"] = study_id
    df["domain"] = domain
    df["source_file"] = source_file
    df["ingestion_time"] = datetime.utcnow()

    return df


def clean_dataframe(
    df: pd.DataFrame,
    study_id: str,
    domain: str,
    source_file: str
) -> pd.DataFrame:
    """
    Full deterministic cleaning pipeline.
    """
    df = df.copy()

    df = normalize_columns(df)
    df = normalize_missing_values(df)
    df = remove_empty_rows(df)
    df = add_metadata(df, study_id, domain, source_file)

    return df
