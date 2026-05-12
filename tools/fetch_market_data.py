import requests
import os

FMP_API_KEY = os.getenv("FMP_API_KEY")

def fetch_market_data_b(ticker: str):
    try:
        url = f"https://financialmodelingprep.com/api/v4/quote?symbol={ticker}&apikey={FMP_API_KEY}"
        print("DEBUG URL:", url)

        response = requests.get(url)

        if response.status_code != 200:
            return None, f"FMP API error: {response.status_code} Text: {response.text}"

        data = response.json()

        if not data:
            return None, f"No market data found for ticker: {ticker}"

        return data[0], None

    except Exception as e:
        return None, str(e)


import yfinance as yf

def fetch_market_data(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info:
            return None, f"No market data found for ticker: {ticker}"

        return info, None

    except Exception as e:
        return None, str(e)
