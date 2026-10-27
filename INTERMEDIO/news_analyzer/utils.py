def get_sources_comprehension(articles):
    # Expresion
    # For member in interable
    # if condition
    return {
        article.get("source_name").get("name")
        for article in articles
        if article.get("source_name") and article.get("source_name").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    print({article["source_name"]["name"] for article in articles})
    return list(
        filter(
            lambda article: article["source_name"]["name"].lower() == source.lower(),
            articles,
        )
    )


def get_reading_time(article: dict) -> dict:
    """Calcula el tiempo de lectura"""
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article
