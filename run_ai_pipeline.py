import pandas as pd
from agents.insight_agent import InsightAgent
from agents.recommendation_agent import RecommendationAgent

ISSUES_PATH = "data/issues/all_issues.csv"

# 1. Load detected issues
df = pd.read_csv(ISSUES_PATH)

# -------------------------------
# 🔹 ADD THIS PART HERE
# -------------------------------
summary_df = (
    df.groupby(["domain", "issue_type", "severity"])
    .size()
    .reset_index(name="count")
    .sort_values(by="count", ascending=False)
)
issues_text = summary_df.to_string(index=False)
# -------------------------------

# 2. Generate insights
insight_agent = InsightAgent()
insights = insight_agent.generate_insights(issues_text)

print("\n=== INSIGHTS ===\n")
print(insights)

# 3. Generate recommendations
recommendation_agent = RecommendationAgent()
recommendations = recommendation_agent.recommend(insights)

print("\n=== RECOMMENDATIONS ===\n")
print(recommendations)
