import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load .env file
load_dotenv()


class RecommendationAgent:
    """
    Recommendation Agent:
    - Operates during ongoing clinical trials (pre-submission)
    - Provides decision-support recommendations only
    - Does NOT make medical, operational, or regulatory decisions
    """

    def __init__(self, model_name="llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            model=model_name,
            temperature=0.3,
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are an expert clinical trial operations decision-support agent.

This system operates during ongoing clinical trials,
before regulatory submission and drug approval.

Your role is to provide DECISION SUPPORT based strictly on provided insights.
You do NOT make final medical, operational, or regulatory decisions.
Final responsibility remains with clinical trial teams.

Using ONLY the insights below, generate structured recommendations.

REQUIREMENTS:
1. Base all recommendations strictly on the provided insights.
2. Prioritize actions by risk and operational impact.
3. Focus on standard clinical trial workflows.
4. Assign responsibilities clearly to relevant teams.
5. Do NOT introduce new problems, risks, or assumptions.
6. Keep recommendations practical, concise, and non-prescriptive.

Output strictly in the following format:

=== RECOMMENDATIONS ===
Immediate Actions (Short-term Operational Steps):
Follow-up Steps (Process or Monitoring Improvements):
Responsible Teams:

Insights:
{insights}
""")


    def recommend(self, insights: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(insights=insights)
        )
        return response.content
