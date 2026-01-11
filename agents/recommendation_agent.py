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
You are a clinical trial operations advisor.

This system operates during ongoing clinical trials,
before regulatory submission and drug approval.

Your role is to provide DECISION SUPPORT only.
You do NOT make final medical, operational, or regulatory decisions.
Final decisions remain with clinical trial teams.

Based ONLY on the insights provided below, suggest:

- Immediate actions (short-term operational steps)
- Follow-up steps (process or monitoring improvements)
- Responsible teams (e.g., CRA, Data Management, Safety)

Keep recommendations practical, non-prescriptive,
and aligned with standard clinical trial operations.
Do not introduce new risks or assumptions.

Insights:
{insights}
""")

    def recommend(self, insights: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(insights=insights)
        )
        return response.content
