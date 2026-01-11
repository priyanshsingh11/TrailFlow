import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load .env file
load_dotenv()


class InsightAgent:
    """
    Insight Agent:
    - Operates during ongoing clinical trials (pre-submission)
    - Explains detected issue patterns
    - Does NOT make decisions or recommendations
    """

    def __init__(self, model_name="llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            model=model_name,
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are a clinical trial data expert.

This system operates during ongoing clinical trials,
before regulatory submission and drug approval.

Your role is to EXPLAIN detected issues for clinical trial teams.
You do NOT make medical, operational, or regulatory decisions.
You do NOT suggest actions or recommendations.

Based only on the issues provided below, summarize:

- Key problem patterns
- Affected clinical domains
- Potential risks to trial execution or data integrity

Keep the explanation concise, factual, and high-level.
Do not introduce information not present in the issues.

Detected Issues Summary:
{issues}
""")

    def generate_insights(self, issues_text: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(issues=issues_text)
        )
        return response.content
