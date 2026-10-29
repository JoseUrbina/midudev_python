# Contador de frecuencia

palabras1  = ["Manzana", "Banana", "manzana", "PERA", "banana", "manzana", "Naranja"]
palabras2 = ["python", "diccionario", "Python", "metodos", "DICCIONARIO", "python", "codigo"]

def contar_frecuencias(lista_palabras):
    diccionario = {}

    for palabra in lista_palabras:
        sanitizada = palabra.lower()

        diccionario[sanitizada] = diccionario.get(sanitizada, 0) + 1

    return diccionario

print(contar_frecuencias(palabras1))
print(contar_frecuencias(palabras2))
