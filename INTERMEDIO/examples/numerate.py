from sample_data import sample_articles

# For tradicional para listar y enumerar los articulos con un iterador
counter = 1
for article in sample_articles:
    # print(f"{counter}: {article}")
    counter = counter + 1


# Enumerate, recibe una lista o iterable
sample_articles_enum = enumerate(
    sample_articles, start=10
)  # Le puedo decir desde cuando quiero que empiece porque si no lo hace desde 0
print(sample_articles_enum)  # Inicialmente lo guarda en memoria para usarlo

# Uso
for counter, article in sample_articles_enum:
    print(f"{counter}:{article}")
