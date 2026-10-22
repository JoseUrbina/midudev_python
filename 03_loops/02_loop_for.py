###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o un lista
###

print("\nBucle for:")

# iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# iterar sobre cualquier cosa que sea iterable
cadena = "midudev"
for caracter in cadena:
    print(caracter)

# enumerate()
for indice, fruta in enumerate(frutas):
    print(f"El índice es {indice} y la fruta es {fruta}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\n--- Break ---")
animales = ["perro", "gato", "ratón", "loro", "pez", "canario"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El {animal} está escondido en el índice {index}")
        break

# continue
print("\n--- Continue ---")
animales = ["perro", "gato", "ratón", "loro", "pez", "canario"]
for animal in animales:
    if animal == "loro": continue

    print(animal)
