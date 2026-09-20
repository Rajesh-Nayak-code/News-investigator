import html

import streamlit as st

from app.agents.claim_analyzer import analyze_claim
from app.agents.research_agent import research_agent
from app.agents.evidence_agent import evidence
from app.agents.verdict_agent import verdict


def format_for_card(text) -> str:
    """Escape text and convert line breaks so it renders safely inside an HTML card."""
    return "<br>".join(html.escape(str(text).strip()).splitlines())


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="TruthLens AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(67, 56, 202, 0.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(37, 99, 235, 0.10), transparent 30%),
        #080a0f;
    color: #e5e7eb;
}


/* Remove default top padding */

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}


/* Header */

.logo {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #8b5cf6;
    margin-bottom: 12px;
}

.title {
    font-size: 42px;
    font-weight: 700;
    letter-spacing: -1.5px;
    color: #f8fafc;
    margin-bottom: 8px;
}

.subtitle {
    color: #8b93a7;
    font-size: 15px;
    margin-bottom: 35px;
}


/* Input */

.stTextArea textarea {
    background: #0d1118 !important;
    color: #f1f5f9 !important;
    border: 1px solid #202633 !important;
    border-radius: 12px !important;
    padding: 18px !important;
    font-size: 15px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #6366f1 !important;
    box-shadow: 0 0 0 1px #6366f1 !important;
}


/* Button */

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    border: 1px solid #6366f1;
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );
    color: white;
    font-size: 15px;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton > button:hover {
    border-color: #8b5cf6;
    box-shadow: 0 0 25px rgba(99, 102, 241, 0.25);
}


/* Section headings */

.section-title {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #a5b4fc;
    text-transform: uppercase;
    margin-top: 30px;
    margin-bottom: 12px;
}


/* Cards */

.card {
    background: rgba(14, 18, 27, 0.88);
    border: 1px solid #202633;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 16px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.20);
}

.card-label {
    color: #737b8f;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.card-value {
    color: #f1f5f9;
    font-size: 15px;
    line-height: 1.7;
}

.card-value + .card-label {
    margin-top: 18px;
}


/* Verdict */

.verdict-card {
    background:
        linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.14),
            rgba(124, 58, 237, 0.05)
        );
    border: 1px solid rgba(99, 102, 241, 0.45);
    border-radius: 16px;
    padding: 25px;
    margin-top: 20px;
}

.verdict-title {
    color: #a5b4fc;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.verdict-content {
    color: #f8fafc;
    font-size: 16px;
    line-height: 1.7;
}


/* Divider */

.divider {
    height: 1px;
    background: #1c222d;
    margin: 35px 0;
}


/* Footer */

.footer {
    text-align: center;
    color: #4b5563;
    font-size: 12px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="logo">TRUTHLENS / AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">News Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Investigate a claim using AI-powered research, evidence analysis, and verdict generation.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CLAIM INPUT
# ============================================================

st.markdown(
    '<div class="section-title">Enter Claim</div>',
    unsafe_allow_html=True
)

user_input = st.text_area(
    "Claim",
    placeholder="Enter a news claim you want to investigate...",
    height=140,
    label_visibility="collapsed"
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze_button = st.button("Investigate Claim")


# ============================================================
# PIPELINE
# ============================================================

if analyze_button:

    if not user_input.strip():
        st.warning("Please enter a claim.")

    else:

        # ----------------------------------------------------
        # CLAIM ANALYSIS
        # ----------------------------------------------------

        with st.spinner("Analyzing claim..."):
            claim_analysis = analyze_claim(user_input)

        st.markdown(
            '<div class="section-title">Claim Analysis</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-label">Detected Claim</div>
                    <div class="card-value">
                        {claim_analysis.claim}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-label">Topics</div>
                    <div class="card-value">
                        {claim_analysis.topics}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="card">
                <div class="card-label">Time Sensitive</div>
                <div class="card-value">
                    {claim_analysis.time_sensitive}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # RESEARCH
        # ----------------------------------------------------

        research_input = f"""
Claim:
{claim_analysis.claim}

Topics:
{claim_analysis.topics}

Time-sensitive:
{claim_analysis.time_sensitive}
"""

        with st.spinner("Researching relevant information..."):
            result = research_agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": research_input
                    }
                ]
            })

        research_content = result["messages"][-1].content[0]["text"]

        st.markdown(
            '<div class="section-title">Research Result</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">
                <div class="card-value">
                    {research_content}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # EVIDENCE ANALYSIS
        # ----------------------------------------------------

        with st.spinner("Analyzing evidence..."):
            ev = evidence(
                claim_analysis.claim,
                research_content
            )

        st.markdown(
            '<div class="section-title">Evidence Analysis</div>',
            unsafe_allow_html=True
        )

        # Convert result to dictionary
        if hasattr(ev, "model_dump"):
            ev_data = ev.model_dump()
        elif hasattr(ev, "dict"):
            ev_data = ev.dict()
        elif isinstance(ev, dict):
            ev_data = ev
        else:
            ev_data = {}

        source_url = ev_data.get("source_url", "Not available")
        key_evidence = ev_data.get("key_evidence", "Not available")
        relationship = ev_data.get("relationship", "Not available")
        strength = ev_data.get("strength", "Not available")
        reasoning = ev_data.get("reasoning", "Not available")

        evidence_fields = [
            ("Source URL", source_url),
            ("Key Evidence", key_evidence),
            ("Relationship", relationship),
            ("Strength", strength),
            ("Reasoning", reasoning),
        ]

        # Built as one unbroken HTML string: blank lines or indentation
        # inside the markup make Streamlit's markdown parser break the card.
        evidence_rows = "".join(
            f'<div class="card-label">{label}</div>'
            f'<div class="card-value">{format_for_card(value)}</div>'
            for label, value in evidence_fields
        )

        st.markdown(
            f'<div class="card">{evidence_rows}</div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # VERDICT
        # ----------------------------------------------------

        with st.spinner("Generating final verdict..."):
            verdict_model = verdict(
                claim_analysis.claim,
                ev
            )

        # Extract actual AI response text
        if hasattr(verdict_model, "content"):

            content = verdict_model.content

            if isinstance(content, list):
                verdict_text = ""

                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        verdict_text += item.get("text", "")

            else:
                verdict_text = str(content)

        else:
            verdict_text = str(verdict_model)

        verdict_html = format_for_card(verdict_text)

        st.markdown(
            '<div class="section-title">Final Verdict</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="verdict-card">'
            f'<div class="verdict-content">{verdict_html}</div>'
            f'</div>',
            unsafe_allow_html=True
        )