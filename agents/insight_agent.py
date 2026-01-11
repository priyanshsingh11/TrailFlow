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
You are an expert clinical trial data analysis agent.

This system operates during ongoing clinical trials,
before regulatory submission and drug approval.

Your role is to ANALYZE and EXPLAIN detected issue patterns.
You do NOT recommend actions.
You do NOT make medical, operational, or regulatory decisions.

Your task is to reason over the detected issues and produce
a structured, high-level explanation for clinical trial teams.

REQUIREMENTS:
1. Identify meaningful patterns across issues (not a simple summary).
2. Indicate the scale or concentration of problems where possible.
3. Clearly state which clinical domains are affected.
4. Explain real-world impact on trial execution, data integrity, audits, or timelines.
5. Do NOT suggest fixes, actions, or next steps.
6. Do NOT introduce information not present in the issues.

Output strictly in the following format:

=== INSIGHTS ===
Summary:
Key Problem Patterns:
Affected Clinical Domains:
Potential Risks to Trial Execution or Data Integrity:

Detected Issues:
{issues}
""")


    def generate_insights(self, issues_text: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(issues=issues_text)
        )
        return response.content
