# Clase 12
class DivisionError(Exception):
    """
    Error en operacion
    """


a = 0
b = 0
try:
    a = int(input("Digita un numero A: "))
    b = int(input("Digita un numero B: "))
except Exception:
    print("No puedes digitar algo diferente a un numero ")

"""
V1: si lo divido por 0 me va a dar error. Con eso paras que no se caiga ponemos el try y el except

resultado = a / b
"""
resultado = None
try:
    resultado = a / b
except Exception as e:
    print(f"No puedes dividir por 0 y usaste {e}")

print(f"resultado: {resultado}")

print(" ")
# Otra versionmpara dejar toda la excepcion
try:
    a = int(input("Digita un numero A: "))
    b = int(input("Digita un numero B: "))
    if b == 2:  # Clase 12: Cómo crear excepciones personalizadas en Python
        raise Exception("No esta permitido el calculo por 2")
    resultado = a / b
    print(f"resultado: {resultado}")
except ValueError:
    print("No puedes digitar algo diferente a un numero ")
except ZeroDivisionError:
    print("No puedes dividir por 0")
finally:
    print(
        "Print desde finally"
    )  # Clase 11: Cómo usar finally para manejar errores en Python


print("Otro print")
