"""
Sistema de analisis de noticias con APIS multiples
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import NEWSAPI_KEY
from news_analyzer.exceptions import APIKeyError

response_data = None
try:
    response_data = fetch_news("newsapi", api_key=NEWSAPI_KEY, query="Apple")
except APIKeyError as e:
    print(e)

if response_data:
    for article in response_data["results"]:
        print(article["title"])
