# AI‑Powered Resume–JD Matching & Grounded Resume Refinement Engine
A modular, agentic AI system built using LangGraph, Reflexion, and schema‑validated LLM pipelines to:
* evaluate how well a resume aligns with a job description
* compute ATS‑style match scores
* identify missing skills, tools, and responsibilities
* generate structured critique
* rewrite resume sections using grounded, drift‑controlled LLM outputs
* export a clean, professional resume document

This project demonstrates production‑grade AI engineering patterns, including multi‑node orchestration, grounding rules, tone‑restraint logic, and deterministic JSON‑schema enforcement.

## Key Features
* Resume–JD Matching
* Extracts skills, tools, and responsibilities from job descriptions
* Computes ATS‑style alignment score
* Highlights missing or weak areas

## Structured Critique Engine
* Generates actionable feedback
* Identifies gaps in skills, tools, and responsibilities
* Provides rewrite guidance without hallucinating

## Grounded Resume Rewriting
* Enforces strict anti‑fabrication rules
* Preserves structure, bullet count, and factual accuracy
* Applies tone‑restraint and contextual‑qualifier rules
* Produces deterministic JSON outputs

## Reflexion Loop
* Iteratively improves the rewritten resume
* Ensures alignment with critique
* Eliminates drift and tone inflation

## Document Export
* Generates a clean, formatted Word document
* Preserves structure and readability

# Architecture Overview
Job Description → JD Parser → ATS Scoring → Critique Generator
                                             ↓
Resume → Resume Parser → Rewrite Engine → Reflexion Loop → Export

## Core Components
* LangGraph multi‑node workflow
* Schema‑validated LLM outputs
* Grounding + tone‑restraint rules
* Factual consistency checks
* Deterministic rewriting pipeline


# ===========================
# REQUIRED API KEYS
# ===========================

# OpenAI API key for LLM calls
OPENAI_API_KEY=

# LangSmith API key for tracing & debugging
LANGSMITH_API_KEY=

# Tavily API key for search tool
TAVILY_API_KEY=

# Pinecone API key for vector storage
PINECONE_API_KEY=


# ===========================
# OPTIONAL / PROJECT SETTINGS
# ===========================

# Enable LangSmith tracing
LANGSMITH_TRACING_V2=true

# LangSmith endpoint (default is fine)
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# Project name for LangSmith traces
LANGSMITH_PROJECT=LangraphCourse

# Pinecone index name
INDEX_NAME=medium-blogs-embeddings-index
