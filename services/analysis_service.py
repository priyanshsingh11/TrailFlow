import pandas as pd
from run_pipeline import run_pipeline
from issue_model.issue_pipeline import detect_issues_from_csv
from agents.insight_agent import InsightAgent
from agents.recommendation_agent import RecommendationAgent


def run_full_analysis(raw_dir: str, processed_dir: str):
    # Step 1: ingestion + cleaning
    run_pipeline(raw_dir, processed_dir)

    # Step 2: issue detection
    all_issues = []
    for file in processed_dir.glob("*.csv"):
        issues = detect_issues_from_csv(str(file))
        for issue in issues:
            all_issues.append(issue.__dict__)

    df_issues = pd.DataFrame(all_issues)

    # Aggregate for AI
    summary_df = (
        df_issues.groupby(["domain", "severity"])
        .size()
        .reset_index(name="count")
    )

    issues_text = summary_df.to_string(index=False)

    # Step 3: AI reasoning
    insight_agent = InsightAgent()
    insights = insight_agent.generate_insights(issues_text)

    recommendation_agent = RecommendationAgent()
    recommendations = recommendation_agent.recommend(insights)

    return {
        "issue_summary": summary_df.to_dict(orient="records"),
        "insights": insights,
        "recommendations": recommendations
    }
