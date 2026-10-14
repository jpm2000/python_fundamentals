import json
import urllib
import urllib.parse
import urllib.request

# Usar la importacion relativa porque esta en el mismo paquete
from .config import BASE_URL
from .exceptions import APIKeyError


# Simulo que tengo la API
def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con {timeout}"


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
