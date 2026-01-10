import pandas as pd
from issue_model.data_quality_issues import detect_data_quality_issues


def detect_issues_from_csv(csv_path: str) -> list:
    df = pd.read_csv(csv_path)

    domain = df["domain"].iloc[0]

    if domain == "data_quality":
        return detect_data_quality_issues(df)

    # Other domains will be added later
    return []
