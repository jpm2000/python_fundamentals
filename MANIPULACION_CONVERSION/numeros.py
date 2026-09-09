from time import process_time_ns


x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

positivo = 5.5
negativo = -5.5
imaginario = -5 - 1j

# Puede que necesitemos cambiar el dato, como el casteo
xf = float(x)  # x ahora se comporta como un flotante
print(type(xf))
print(xf)

ye = int(y)
print(type(ye))
print(ye)

# Puedo castear un complejo? Si se pueden mover los enteros a complejos
entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))
print(flotanteComplejo)
print(type(flotanteComplejo))

import random

print(random.randrange(1, 10))  # Va a buscar un numero aleatorio
