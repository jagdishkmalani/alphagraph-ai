from tavily import TavilyClient
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=TAVILY_API_KEY)

def fetch_news(ticker: str):
    try:
        query = f"{ticker} stock news"
        response = client.search(query=query, max_results=5)

        if "results" not in response:
            return None, "No news results returned"

        news_items = []
        for item in response["results"]:
            news_items.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "content": item.get("content"),
                "score": item.get("score"),
            })

        return news_items, None

    except Exception as e:
        return None, str(e)
