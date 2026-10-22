# Comprensión de listas (list comprehension)

animales = ["perro", "gato", "loro", "león", "elefante", "cocodrilo"]

# lista con todos los animales en mayúsculas

animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista

numeros_pares = [numero for numero in [0, 1, 2, 3, 4, 5, 6] if numero % 2 == 0]

print(numeros_pares)

