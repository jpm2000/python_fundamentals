"""
Clase 15: como utilizar los docstrings

Por ejemplo esto me va a servir mucho para generar documentacion
"""


def ejemplo_sin_docstring():
    return "Hola mundo"


def ejemplo_con_docstring():
    """
    DESCRIPCION
    Esta funcion devuelve un saludo.

    ARGUMENTOS

    RETURNS
    Returns:
        str: Un saludo en español

    EXCEPTIONS

    EXAMPLES
    """
    return "Hola mundo"


# Como acceder a la documentacion desde el codigo
print(ejemplo_con_docstring.__doc__)

# Otra forma de acceder
help(ejemplo_con_docstring)
