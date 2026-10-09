# Toda la ejecucion del codigo en un archivo
"""
Sistema de analisis de noticias financieras con APIs multiples
"""

# PEP 8: Configuracion cnetralizada - constantes en MAYUSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: comillas dobles para los strings


# PEP 8: Utilidades comunes del proyecot - funciones en snake_case
def clean_text(text):
    # PEP 8: Usar siempre 4 espacios por identacioin, no tabs
    """Limpia y normaliza el texto."""  # PEP 8: docstrings en comillas doblres triples
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble lineas en blanco entre funciones para separar logicamente
def variabe_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales deben estar agrupadas despues de la utilidades
def fecth_news_from_api(api_name, query):
    """Obtiene noticias de una API especifica."""


def process_article_data(raw_data):
    """Procesa datos crudos de articulo"""


# Clase 7: Python *args: Variable Function Arguments


# Traer el API de las noticias

# Clase 9: Conectar Python a NewsAPI con parámetros reales

import json
import urllib.parse
import urllib.request


class NewsSystemError(Exception):
    """
    Error general en la app
    """


class APIKeyError(NewsSystemError):
    """
    Error cuando la API KEY es invalida
    """


# import requests

NEWSAPI_KEY = "pub_e84fe709ba3a44c7905e324540f98d691"
BASE_URL = (
    "https://newsdata.io/api/1/market?apikey=pub_e84fe709ba3a44c7905e324540f98d69"
)

# Tuvo unas modificaciones en la clase 9


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})

    # print(query_string) solo para validar
    url = (
        f"{BASE_URL}?{query_string}"  # Aca le sumo los parametros que le voy agregando
    )

    # print(url) solo para validar
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode(
                "utf-8"
            )  # Estoy recibiendo bytes, entonces uso decode. Por lo que viene en json
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrio un error, no se conecto la API")

        # print("La API kEY es invalidad") clase 11
        # return {"results": []} clase 11
        # Ya no usaré esta parte: print(f"Response data: {data[:100]}...")  # Imprime los primeros 100 caracteres

    return f"NewsAPI: {query} con timeout {timeout}"


"""
Version clase 7
def newsapi_client(api_key, query, timeout=30, retries=3):
    return f"NewsAPI: {query} con timeout {timeout}"
"""


# Simulo que tengo la API
def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con {timeout}"


# El orden si importa cuando trabajo con estas funciones y los args
# Los args son las listas dinamicas
print("args")


def ejemplo_args(api_key, *args):
    print(f"api key: {api_key}")
    print(f"TODOS {args}")
    print(f"{type(args)}")


# Representacion de una tupla
ejemplo_args("API_KEY_VALUE", "Este", "Parametro", "Aca")
ejemplo_args("API_KEY_VALUE", "Hola", "Mundo")
# ejemplo_args() # Si no lo envio va a fallar


# Uso de args para hacer la suma
def suma(*args):
    return sum(args)


print(suma(1, 2, 3, 4, 5, 6, 6, 7))

# Ahora para kwargs
print(" ")
print("kwargs")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs type: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("========")


# Le paso key y el value
ejemplo_kwargs(key="value", llave="valor")
# Es un tipo de diccionario, donde esta la llave y el valor. Como tal la funcion no recibe un valor, solo los kwargs


ejemplo_kwargs(api_key="DEMO", query="Nocitias de python", timeout=30, retries=3)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN", section="Sports", from_date="20", timeout=30, retries=3
)

# Es un solo metodo al que le podemos agregar varios valores y parametros


# El orden siempre importa, lo obligatorio va primero
def fetch_news(api_name, *args, **kwargs):
    """
    Funcion flexible para conectar con el API
    """
    base_config = {"timeout": 30, "retries": 3}

    config = {
        # Pasar los valores de base config con **base_config
        **base_config,
        **kwargs,
    }

    api_clients = {"newsapi": newsapi_client, "guardian": guardian_client}

    client = api_clients[api_name]
    # Usar doble ** es como pasar los valores internamente
    return client(*args, **config)


"""
NEWSAPI_KEY = "pub_e84fe709ba3a44c7905e324540f98d69"

url = "https://newsdata.io/api/1/market?apikey=pub_e84fe709ba3a44c7905e324540f98d69"
response = requests.get(url)
data = response.json()
# print(data)

fetch_news(NEWSAPI_KEY, "Informacion de la API: ", url=url, data_response=data)

"""

# Ahora quiero recibir una lista directa de los resultados o articles
# print(response_data["results"])


response_data = None
try:
    response_data = fetch_news("newsapi", api_key=NEWSAPI_KEY, query="Apple")
except APIKeyError as e:
    print(e)
# print(response_data) impprime todo
if response_data:
    print(
        response_data.keys()
    )  # para ver las llaves que estoy recibiendo en el servidor

if response_data:
    for article in response_data["results"]:
        print(article["title"])
