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


# Otra versionmpara dejar toda la excepcion
try:
    a = int(input("Digita un numero A: "))
    b = int(input("Digita un numero B: "))
    resultado = a / b
except ValueError:
    print("No puedes digitar algo diferente a un numero ")
except ZeroDivisionError:
    print("No puedes dividir por 0")
