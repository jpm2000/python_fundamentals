# El for es un iterador

from time import process_time_ns


palabra = "python"

for letra in palabra:
    print(letra)  # va a imprimir todas las letras


frutas = ["manzana", "naranja", "kiwi"]

for f in frutas:
    if f == "naranja":
        break
    print(f)

for f in frutas:
    if f == "naranja":
        continue
    print(f)
else:
    print("Ya se termino el bucle")

print(" ")

for i in range(10):
    print(i)  # 10 no esta incluido en el bucle

for i in range(3, 10):
    print(i)  # entre el 3 y el 9

for i in range(0, 10, 2):
    print(i)

# Bucle anidado
adjetivos = ["rica", "saludadble"]

for a in adjetivos:  # lo que se repite inicialmente es el adjetivo
    for f in frutas:
        print(f, a)

for f in frutas:
    for a in adjetivos:
        print(f, a)

for i in range(10):
    pass
