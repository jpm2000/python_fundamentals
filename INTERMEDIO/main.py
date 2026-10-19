"""
Sistema de analisis de noticias con APIS multiples
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import NEWSAPI_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import get_articles_by_source, get_sources_comprehension

response_data = None
try:
    response_data = fetch_news("newsapi", api_key=NEWSAPI_KEY, query="Apple")
except APIKeyError as e:
    print(e)

if response_data:
    sources_set = get_sources_comprehension(response_data["results"])

    for index, source in enumerate(sources_set, start=1):
        print(f"No: {index} -- {source}")

    for article in response_data["results"]:
        print(article["title"])

    articulos_ejemplo = get_articles_by_source(response_data["results"], "Bloomberg")
    for eje_article in articulos_ejemplo:
        print(articulos_ejemplo["source"], articulos_ejemplo["title"])
