from state.state                 import AlphagraphState
def input_validation_node(state: AlphagraphState) -> AlphagraphState:
    ticker = state.get("ticker")

    if not ticker:
        return {"errors": ["Ticker is required"]}

    ticker = ticker.upper()

    if not ticker.isalpha():
        return {"errors": [f"Invalid ticker format: {ticker}"]}

    return {"ticker": ticker}
