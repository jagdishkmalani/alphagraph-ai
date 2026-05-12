from state.state import AlphagraphState
from tools.run_analysis_llm import run_analysis_llm
import json

def analysis_node(state: AlphagraphState) -> AlphagraphState:
    ticker = state.get("ticker")
    market_data = state.get("market_data")
    news_data = state.get("news_data")

    if not ticker or not market_data or not news_data:
        return {"errors": ["Missing data for analysis"]}

    analysis, error = run_analysis_llm(ticker, market_data, news_data)

    if error:
        return {"errors": [error]}

    try:
        analysis_json = json.loads(analysis)
    except:
        analysis_json = {"raw_output": analysis}

    return {"llm_output": analysis_json}
