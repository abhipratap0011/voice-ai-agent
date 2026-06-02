import os
import yfinance as yf
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str) -> str:
    results = tavily.search(query=query, max_results=3)
    output = []
    for r in results.get("results", []):
        output.append(f"{r['title']}: {r['content']}")
    return "\n".join(output)


def get_stock_price(ticker: str) -> str:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")
        if not hist.empty:
            price = round(hist["Close"].iloc[-1], 2)
            return f"{ticker} current price is ${price}"
        else:
            result = web_search(f"{ticker} stock price today")
            return result
    except Exception:
        result = web_search(f"{ticker} stock price today")
        return result