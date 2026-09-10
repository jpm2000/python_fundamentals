# Mientras la condicion se cumpla

i = 1
while i < 10:
    print(i)
    i += 1  # En cada bucle se aumenta 1 el i, menor a 10

x = 1

while x <= 10:
    print(x)
    x += 1  # En cada bucle se aumenta 1 el i, menor o igual a 10

y = 1

# ROmper el bucle
while y <= 10:
    print(y)
    if y == 5:
        break
    y += 1

z = 1

# Llega a 11 porque dice que si llega a 10 aumente uno mas
while z <= 10:
    z += 1
    print(z)

w = 0
while w < 10:
    if w == 5:
        break
    w += 2
    print(w)

# Continue para saltar la instruccion

t = 0
while t < 10:
    t += 1
    if t == 5:  # no incluye el 5
        continue
    print(t)
else:
    print("t dejo de ser menor a 10")
