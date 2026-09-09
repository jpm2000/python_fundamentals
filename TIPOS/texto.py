multiplesLineas = """
se va a respetar tambien en la temrinal
Que se saltan las lineas
"""

print(multiplesLineas)

palabra = "murcielago"
print(len(palabra))

texto = "Este curso es de fundamentos de python"
# Python va a interpretar si esa palabra esta en el texto, con un booleano
estaIncluida = "python" in texto
noEstaIncluida = "Javascript" not in texto

print(estaIncluida)
print(
    noEstaIncluida
)  # Va a dar verdadero porque no esta incluido en el texto, o sea la loguca es verdadera

# Manupular texto
mayus = texto.upper()
minus = texto.lower()

print(mayus)
print(minus)

texto2 = texto.upper()
print(texto2)
texto2 = texto.lower()  # la ultima es la prevalece
print(texto2)

espacios = "      espacios en la variables    "
sinEspacio = espacios.strip()
print(sinEspacio)
