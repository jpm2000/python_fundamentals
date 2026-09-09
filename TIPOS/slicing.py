# Saber donde cortar

# in: la psicion siempre empieza desde 0. Los espacio tambien cuentan
from traceback import print_tb


texto = "este es un texto"

print(texto[0])
print(texto[4])
print(texto[0:10])
print(texto[0:15])  # La "o" no esta incluido, esto pasa con el ultimo valor
print(texto[:16])  # no necesito el 0 en el incio del slicing
print(texto[5:])
print(texto[5:-2])

curso = "Este curs es de javascript, javascript otra vez"
print(curso)
print(
    curso.replace("javascript", "python")
)  # funciona para todas las veces que diga la palabra a reemplazar

# Metdo split

textoDividido = texto.split(" ")
print(textoDividido)  # Cada palabra se vuelve un elemeto

texto3 = "Este es un texto  que tiene MAYUSCULAS Y minusculas, ahora encontremoslas"
print("mayusculas".lower() in texto3.lower())
