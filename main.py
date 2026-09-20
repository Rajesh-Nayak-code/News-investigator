from app.agents.claim_analyzer import analyze_claim
from app.agents.research_agent import research_agent
from app.agents.evidence_agent import evidence
from app.agents.verdict_agent import verdict

user_input=input("enter input")

claim_analysis = analyze_claim(user_input)

print("CLAIM ANALYSIS")
print(claim_analysis)


research_input = f"""
Claim:
{claim_analysis.claim}

Topics:
{claim_analysis.topics}

Time-sensitive:
{claim_analysis.time_sensitive}
"""


# Step 3: Research
result = research_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": research_input
        }
    ]
})

research_content = result["messages"][-1].content[0]["text"]

ev=evidence(claim_analysis.claim,research_content)
verdict_model=verdict(claim_analysis.claim,ev)

print("\nRESEARCH RESULT")
print(research_content)

print("\n")
print("="*50)

print("\nEvidance analysis\n")
print(ev)

print("\n")
print("="*50)

print("\nVerdict\n")
print(verdict_model)