def get_sources_comprehension(articles):
    # Expresion
    # For member in interable
    # if condition
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    return list(filter(lambda article: article["source"]["name"] == source, articles))
