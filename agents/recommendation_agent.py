import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load .env file
load_dotenv()


class RecommendationAgent:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            model=model_name,
            temperature=0.3,
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are a clinical trial operations advisor.

Based on the insights below, recommend:
- Immediate actions
- Follow-up steps
- Responsible teams (CRA, Data Management, Safety)

Insights:
{insights}
""")

    def recommend(self, insights: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(insights=insights)
        )
        return response.content
