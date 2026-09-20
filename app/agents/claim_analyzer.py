from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_classic.prompts import ChatPromptTemplate
load_dotenv()

class Claim_analyzer(BaseModel):
    claim:str=Field(...,description="what is the claim")
    topics:list[str]=Field(...,description="contains topic related to the query")
    time_sensitive:bool=Field(...,description="checks if the topic is time dependent or not")

llm=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

structured_llm=llm.with_structured_output(Claim_analyzer)

def analyze_claim(user_input: str):
   prompt = f"""
    You are the Claim Analyzer Agent in an AI fact-checking system.

    Analyze this user input:

    {user_input}

    Tasks:
    1. Identify the main factual claim.
    2. Identify the main topics.
    3. Determine whether the claim is time-sensitive.

    Do NOT determine whether the claim is true or false.
    """
   return structured_llm.invoke(prompt)
