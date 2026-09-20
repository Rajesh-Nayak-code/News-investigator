# News-investigator

An AI-powered news investigation application that analyzes claims using web search, evidence retrieval, and Large Language Models (LLMs).

## Overview

AI News Investigator helps users investigate news claims by retrieving relevant information from the web, analyzing supporting evidence, and generating a structured verdict.

The application classifies claims into four categories:

* TRUE
* FALSE
* PARTIALLY TRUE
* UNVERIFIABLE

## Features

* **AI-Powered Claim Investigation:** Analyze news claims using LLMs.
* **Web Search Integration:** Retrieve relevant sources using the Tavily Search API.
* **Evidence Analysis:** Collect and analyze information from retrieved sources.
* **Structured Verdicts:** Generate standardized claim classifications.
* **Interactive UI:** Investigate claims through a Streamlit application.


## 🔄 Workflow

1. User enters a news claim.
2. The application searches for relevant information using Tavily.
3. Relevant web content is retrieved for analysis.
4. The LLM evaluates the available evidence.
5. A structured verdict is generated.
6. The investigation results and supporting evidence are displayed in Streamlit.


## ⚠️ Limitations

* AI-generated verdicts may contain errors.
* Search results depend on source availability and relevance.
