sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solol los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solol los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 10]


# Sacar el titulo y la descripcion
def extract_article_summaries(articles):
    """Se crea un nuevo objeto donde se muestra el titulo y la descripcion"""
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


print(extract_titles_traditional(sample_articles))
print("------")
print(extract_titles(sample_articles))
print("------")
print(extract_article_summaries(sample_articles))
