# Clase 5
name = "Ana"
text = f"Hola {name}"
print(text)

text_suma = f"La suma es de {5 + 10}"
print(text_suma)

text_func = f"Hola {name.upper()}"

print(text_func)

edad = 20
text_if = f"{name} es {'mayor' if edad >= 18 else 'menor'} de edad"

print(text_if)

# Clase 6
# Modificadores de formato en f-strings de Python
bank_balance = 1200000000000
text = f"Tu saldo en la cuenta es: {bank_balance:,}"  # La coma se usa para separar miles y una persona lo pueda leer
print(text)

stock_price = 1.405
text = f"El valor de la accion es: {stock_price:.2f}"  # el .2f se usa para redondear a 2 decimales
print(text)

user_id = 1
text = f"El id del usuario es: {user_id:010d}"  # el 010d agrega 10 ceros antes del user id. Es decirle que lo maximo de caracteres que se pueden mostrar son 10
print(text)

product = "Laptop"
price = 1000
text = f"Producto: {product:>15} | Precio: {price:<15} "  # el <15 me permie alinear a la izquierda y que ocupe 15 caracteres
print(f"{text}\n{text}")  # \n es un salto de linea


# Imprimir fechas
from datetime import datetime

date = datetime(2026, 10, 24, 8, 30)
text = f"la fecha de mi cumpleaños es: {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)

date_today = datetime.now()
text = f"todya is: {date_today: %A %d de %B de %Y a las %I:%M %p}"
print(text)

# Formatear un porcentaje y un numero cientifico
porcentaje = 0.2344566
text = f"El porcentaje es: {porcentaje:.2%}"
print(text)

text = f"El porcentaje es: {porcentaje:.4%}"
print(text)

cientifico = 10000000000000000000000000000
text = f"El numero con notacion cientifica es: {cientifico:.2e}"
print(text)

cientifico = 1123227823628934298374892347982374928374
text = f"El numero con notacion cientifica es: {cientifico:.10e}"
print(text)
