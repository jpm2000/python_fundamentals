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


def extract_category(articles):
    """Extrae solo las categorias usando un comprehension"""
    return [
        article["title"] for article in articles if article["category"] == "Ciencia"
    ]


# Sacar el titulo y la descripcion
def extract_article_summaries(articles):
    """Se crea un nuevo objeto donde se muestra el titulo y la descripcion"""
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


# Trae el source y el titulo de los articulos
def extract_source_and_title(articles):
    """Se crea un nuevo objeto donde se muestra el titulo y el source"""
    return {
        article["title"]: article["source"]["name"]
        for article in articles
        if article["source"]["name"] == "TechNews"
    }


print(extract_titles_traditional(sample_articles))
print("------")
print(extract_titles(sample_articles))
print("------")
print(extract_article_summaries(sample_articles))
print("------")
print(extract_category(sample_articles))
print("------")
print(extract_source_and_title(sample_articles))

print("------")
print("Ejercicio")

"""
Como reto, crea una lista sin elementos repetidos de todas las fuentes de tus artículos usando un set. Empieza con la versión tradicional y luego conviértela a una comprensión con conjuntos [09:15]. Comparte tu código en los comentarios para generar discusión y ayudar a otros estudiantes.
"""


# Sources tradicional
def extract_sources_traditional(articles):
    sources = []
    for article in articles:
        if article["source"]["name"] not in sources:
            sources.append(article["source"]["name"])
    return sources


print(extract_sources_traditional(sample_articles))


# Sources con list comprehension
def extract_sources_comprehension(articles):
    return [article["source"]["name"] for article in articles]


print(extract_sources_comprehension(sample_articles))


def extract_unique_sources_comprehension(articles):
    """ "Extrae solo las fuentes usando dict.fromkeys() para eliminar los duplicados"""
    return [dict.fromkeys(article["source"]["name"] for article in articles)]


print(extract_unique_sources_comprehension(sample_articles))

# Como lo soluciona el profesor


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source").get("name") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


print(get_sources_traditional(sample_articles))


def get_sources_comprehension(articles):
    # Expresion
    # For member in interable
    # if condition
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


print(get_sources_comprehension(sample_articles))


# Se requiere hacer iteraciones anidadas
def categorizar_tradicional(articles):
    sources = get_sources_comprehension(articles)
    # Retornar un diccionario
    results = {}
    for source in sources:
        # Agregar un conicional para ver si esta el source o tengo que agregarlo
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)
    return results


print(categorizar_tradicional(sample_articles))


# Categorizar con comprehension
def cateforizar_comprehension(articles):
    sources = get_sources_comprehension(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(cateforizar_comprehension(sample_articles))
