from state.state import AlphagraphState
from tools.fetech_news import fetch_news

def news_retrieval_node(state: AlphagraphState) -> AlphagraphState:
    ticker = state.get("ticker")

    if not ticker:
        return {"errors": ["Ticker missing before news retrieval"]}

    news, error = fetch_news(ticker)

    if error:
        return {"errors": [error]}

    return {"news_data": news}
