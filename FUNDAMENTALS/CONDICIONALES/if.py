if 5 > 3:
    print("5 es mayor a 3")

if 2 > 3:
    print("2 es mayor a 3")

x = 5
y = 3
z = 1

if x > y:
    print(f"{x} es mayor a {y}")
elif x == y:
    print(f"{x} es igual a {y}")
else:
    print("Ninguno se cumplio")


if x > y or x > z:
    print(f"{x} es mayor a {y} y a {z}")
elif x == y:
    print(f"{x} es igual a {y}")
else:
    print("Ninguno se cumplio")

a = "python"
b = "java"
c = "python"

if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")

if a == c:
    print("a es igual a c")
else:
    print("a no es igual a c")

# if anidado
if a == c:
    if a != b:
        print("a es igual a c y no a b")
    else:
        print("else del if interno")
else:
    print("a no es igual a c")

e = 10
f = 10

# Para dejar el if vaío
if e == f:
    pass  # Para definir el comportamiento que se espera mas adelante
