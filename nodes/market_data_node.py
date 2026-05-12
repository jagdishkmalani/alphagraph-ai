from state.state import AlphagraphState
from tools.fetch_market_data import fetch_market_data

def market_data_node(state: AlphagraphState) -> AlphagraphState:
    ticker = state.get("ticker")

    if not ticker:
        return {"errors": ["Ticker missing before market data step"]}

    data, error = fetch_market_data(ticker)

    if error:
        return {"errors": [error]}

    return {"market_data": data}
