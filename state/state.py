from typing import TypedDict, List, Dict, Any, Optional

class AlphagraphState(TypedDict, total=False):
    # User input
    ticker: str

    # Data retrieved from tools
    market_data: Optional[Dict[str, Any]]
    news_data: Optional[List[Dict[str, Any]]]
    rag_chunks: Optional[List[Dict[str, Any]]]

    # Intermediate processing
    assembled_context: Optional[str]

    # Final LLM output
    llm_output: Optional[Dict[str, Any]]

    # Error tracking
    errors: List[str]

"""
Explanation : Optional[List[Dict[str, Any]]]
1. Optional[...]
Means the field may be: None (before the news agent runs) OR a real value (after the news agent runs)
This is important because LangGraph state starts empty and gets filled step‑by‑step.

2. List[...]
Means the value is a Python list. 
Why? Because news retrieval returns multiple articles, not a single string.

3. Dict[str, Any]
Means each item in the list is a dictionary with: keys of type str, values of type Any (because APIs return mixed types)
"""