from openai import OpenAI
import os
from utils.pretty_print import pretty_print
from utils.get_call_cost import get_call_cost

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def run_analysis_llm(ticker, market_data, news_data):
    try:
        prompt = f"""
You are a financial analyst. Analyze the following data for {ticker}.

MARKET DATA:
{market_data}

NEWS DATA:
{news_data}

Provide a structured JSON analysis with:
- company_overview
- recent_news_summary
- sentiment
- risks
- opportunities
- investment_thesis
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        #pretty_print(response.usage)
        get_call_cost(response)
        return response.choices[0].message.content, None

    except Exception as e:
        return None, str(e)
