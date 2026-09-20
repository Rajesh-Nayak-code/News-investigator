from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI

class Evidence(BaseModel):
    source_url: str = Field(
        description="URL of the source"
    )

    key_evidence: str = Field(
        description="Important evidence from the source relevant to the claim"
    )

    relationship: str = Field(
        description="Whether the source supports, contradicts, or is neutral toward the claim"
    )

    strength: str = Field(
        description="Strength of the evidence: HIGH, MEDIUM, or LOW"
    )

    reasoning: str = Field(
        description="Why this evidence supports, contradicts, or is neutral toward the claim"
    )

llm=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

structured_llm=llm.with_structured_output(Evidence)

def evidence(claim:str,research_results=str):
    prompt = f"""
    You are the Evidence Analyzer Agent in an AI fact-checking system.

    Your job is to analyze research collected from web sources.

    CLAIM:
    {claim}

    RESEARCH RESULTS:
    {research_results}

    For each relevant source:

    1. Identify the important evidence related to the claim.
    2. Determine whether the evidence:
    - supports the claim
    - contradicts the claim
    - is neutral
    3. Rate evidence strength:
    - HIGH
    - MEDIUM
    - LOW
    4. Explain your reasoning.

    IMPORTANT RULES:

    - Do NOT give a final TRUE or FALSE verdict.
    - Do NOT invent information.
    - Only use information present in the research results.
    - Ignore evidence that is unrelated to the claim.
    - Prefer official, government, scientific, and highly reputable sources.
    - Clearly distinguish between what the source says and your interpretation.
    """
    return structured_llm.invoke(prompt)

