from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

def verdict(claim:str,evidence:str):
    prompt=f"""You are the Verdict Agent in an AI fact-checking system.

    Your job is to determine the truthfulness of a factual claim
    using ONLY the evidence provided by the Evidence Analyzer.

    CLAIM:
    {claim}

    EVIDENCE:
    {evidence}

    Evaluate the claim carefully.

    Choose exactly ONE verdict:

    - TRUE
    The evidence strongly supports the claim.

    - FALSE
    The evidence strongly contradicts the claim.

    - PARTIALLY TRUE
    The claim contains some correct information but is
    misleading, exaggerated, or partially incorrect.

    - UNVERIFIABLE
    There is not enough reliable evidence to determine
    whether the claim is true or false.

    Rules:

    1. Base your verdict ONLY on the provided evidence.
    2. Do NOT invent facts.
    3. Do NOT perform additional research.
    4. Give more weight to reliable sources such as:
    - Government organizations
    - Official institutions
    - Scientific organizations
    - Research papers
    - Reputable news organizations
    5. Do not assume that a claim is true just because a source
    reports the claim.
    6. Distinguish between evidence supporting the claim and
    evidence merely discussing the topic.
    7. If reliable sources disagree, explain the disagreement.
    8. If the evidence is insufficient, use UNVERIFIABLE.
    9. Provide a short explanation for your verdict.
    10. Mention the strongest evidence that led to your decision.

    Return:
    - verdict
    - confidence
    - explanation
    - key_evidence
    """
    return llm.invoke(prompt)