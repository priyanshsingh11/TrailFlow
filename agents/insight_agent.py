import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load .env file
load_dotenv()


class InsightAgent:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        self.llm = ChatGroq(
            model=model_name,
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are a clinical trial data expert.

Summarize the following detected issues:
- Key problem patterns
- Affected domains
- Potential risks

Issues:
{issues}
""")

    def generate_insights(self, issues_text: str) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(issues=issues_text)
        )
        return response.content
