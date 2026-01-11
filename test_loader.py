# /ONLY FOR THE TESTING PURPOSES/------>

from ingestion.loader import load_excel

df = load_excel(
    r"data\raw\Study 1_CPID_Input Files - Anonymization\Study 1_Compiled_EDRR_updated.xlsx"
)


print("Shape:", df.shape)
print("First 10 columns:", df.columns.tolist()[:10])
print(
    "Sheets:",
    df["_sheet_name"].unique() if "_sheet_name" in df else "Single sheet"
)
