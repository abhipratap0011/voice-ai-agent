import os
import json
from dotenv import load_dotenv
from groq import Groq
from agent.tools import web_search

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful voice assistant. 
Keep answers concise and conversational — 2 to 3 sentences maximum.
You are being spoken aloud so never use markdown, bullet points, or lists.
Just speak naturally like a human assistant would."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for current information, news, stock prices, or anything you don't know",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


SEARCH_KEYWORDS = ["today", "latest", "current", "price", "news", "now", "recent", "score", "weather", "stock"]

def respond(transcript: str, history: list) -> str:
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages += history
        messages.append({"role": "user", "content": transcript})

        needs_search = any(word in transcript.lower() for word in SEARCH_KEYWORDS)

        if needs_search:
            search_result = web_search(transcript)
            messages.append({
                "role": "system",
                "content": f"Here is relevant web search result: {search_result[:2000]}"
            })

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"