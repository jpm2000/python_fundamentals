"""
Typing con python
"""

variable = 42  # int
print(f"Variable: {variable}, del tipo: {type(variable)}")

variable = "Texto de prueba"
print(f"Variable: {variable}, del tipo: {type(variable)}")

# Variable: tipo = valor -> como crearle etiquetas a un frasco
otra_variable: int = 44
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

# Pueden haber casos donde una variable tiene que estar vacia pero si debo asignarle un tipo de dato
user_id: int | None = (
    None  # Usar el operador pyline, para que una variable con none podria estar asignada
)


# Clase 14: Type Hints for Functions and Lists in Python
def suma_clara(a: int, b: int) -> int:
    return a + b


"""
Muy util para saber que datos debo usar cuando tengo una aplicaicon muy grande o con muchos datos
"""

print(suma_clara(1, 2))

articles: list[dict] = [
    {"title": "Example 1"},
    {"title": "Example 2"},
]  # Agrego el [dict], para decir el tipo de lista que es, si agrego un valor que no esta usando la estructura llave y valor de diccionario, da un error
# Cuando uso articles ya el editor me va a mostrar sugerencias de codigo para listas, porque puse el hint
# Por ejemplo, article.append

# Puedo decir que una lista puede estar dentro de otra list[list]

articles_dos: list[list[str]] = [
    ["articulos", "otros"],
    ["mas strings", "otro"],
    ["no puedo poner numeros directo", "deje la lista para strings"],
]

# int, str, tuple, list, dict, Any (validar cualquier tipo de dato)

from typing import Any  # La idea no es abusar del Any

articles_dos: list[list[Any]] = [
    ["articulos", "otros"],
    ["mas strings", "otro"],
    ["no puedo poner numeros directo", "deje la lista para strings"],
]
