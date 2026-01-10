import os
import pandas as pd
from issue_model.issue_pipeline import detect_issues_from_csv

PROCESSED_DIR = "data/processed"
ISSUES_DIR = "data/issues"

os.makedirs(ISSUES_DIR, exist_ok=True)

all_issues = []

for file in os.listdir(PROCESSED_DIR):
    if not file.endswith(".csv"):
        continue

    csv_path = os.path.join(PROCESSED_DIR, file)
    issues = detect_issues_from_csv(csv_path)

    for issue in issues:
        all_issues.append(issue.__dict__)

if all_issues:
    df_issues = pd.DataFrame(all_issues)
    df_issues.to_csv(f"{ISSUES_DIR}/all_issues.csv", index=False)
    print(f"Saved {len(df_issues)} issues to data/issues/all_issues.csv")
else:
    print("No issues detected")
