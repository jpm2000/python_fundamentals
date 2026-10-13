# Clase 20: Dividir el codigo en modulos -> debo tener un modulo separado con los ejemplos


# El orden si importa cuando trabajo con estas funciones y los args
# Los args son las listas dinamicas
print("args")


def ejemplo_args(api_key, *args):
    print(f"api key: {api_key}")
    print(f"TODOS {args}")
    print(f"{type(args)}")


# Representacion de una tupla
ejemplo_args("API_KEY_VALUE", "Este", "Parametro", "Aca")
ejemplo_args("API_KEY_VALUE", "Hola", "Mundo")
# ejemplo_args() # Si no lo envio va a fallar


# Uso de args para hacer la suma
def suma(*args):
    return sum(args)


print(suma(1, 2, 3, 4, 5, 6, 6, 7))

# Ahora para kwargs
print(" ")
print("kwargs")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs type: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("========")


# Le paso key y el value
ejemplo_kwargs(key="value", llave="valor")
# Es un tipo de diccionario, donde esta la llave y el valor. Como tal la funcion no recibe un valor, solo los kwargs


ejemplo_kwargs(api_key="DEMO", query="Nocitias de python", timeout=30, retries=3)
ejemplo_kwargs(
    api_key="DEMO_GUARDIAN", section="Sports", from_date="20", timeout=30, retries=3
)
