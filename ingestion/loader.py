import pandas as pd


def load_excel(file_path: str):
    """
    Loads an Excel file safely.

    - Supports single or multiple sheets
    - Preserves raw values
    - Adds _sheet_name if needed
    - Returns None if no usable data is found
    """

    try:
        excel_file = pd.ExcelFile(file_path)
        sheets = excel_file.sheet_names

        frames = []

        for sheet in sheets:
            df = pd.read_excel(
                file_path,
                sheet_name=sheet,
                dtype=object
            )

            # Skip empty sheets
            if df.empty:
                continue

            # Track sheet source if multiple sheets exist
            if len(sheets) > 1:
                df["_sheet_name"] = sheet

            df.columns = df.columns.str.strip()
            frames.append(df)

        if not frames:
            return None

        return pd.concat(frames, ignore_index=True)

    except Exception as e:
        raise RuntimeError(f"Failed to load Excel file {file_path}: {e}")
