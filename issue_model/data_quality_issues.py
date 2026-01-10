import pandas as pd
from issue_model.schema import Issue
from issue_model.base import generate_issue_id, now


def detect_data_quality_issues(df: pd.DataFrame) -> list[Issue]:
    issues = []

    # Safety check
    if df.empty:
        return issues

    study_id = df["study_id"].iloc[0]
    source_file = df["source_file"].iloc[0]

    # Rule 1: High missing percentage in columns
    missing_ratio = df.isna().mean()

    for column, ratio in missing_ratio.items():
        if ratio > 0.3:  # 30% threshold
            issues.append(
                Issue(
                    issue_id=generate_issue_id(),
                    study_id=study_id,
                    domain="data_quality",
                    issue_type="high_missing_rate",
                    severity="medium",
                    description=f"Column '{column}' has {int(ratio * 100)}% missing values",
                    entity_id=None,
                    source_file=source_file,
                    detected_at=now(),
                )
            )

    return issues
