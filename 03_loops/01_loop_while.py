###
#   01 - Bucles (while)
#   Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
###

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# utilizando la palabra break para romper el bucle

print("\nBucle while con break:")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # rompe el bucle

# obtener el primer número < 100 y múltiplo de 5

contador = 0

while contador <= 100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        print("El número es múltiplo de 5")
        break

# continue, salta esa iteración en concreto y continua con el bucle

# imprime los número impares menores a 10

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)
else:
    print("El ciclo while ha finalizado.")

# else

print("\nBucle while con else")

contador = 5

while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# pedirle al usuario un número que tiene que ser positivo

numero = -1

while numero < 0:
    try:
        numero = int(input("Ingrese un número positivo: "))

        if numero <= 0:
            print("El número ingresado no es positivo, intenta otra vez.")
    except Exception:
        print("Ha ocurrido un error, intenta otra vez.")

print(f"El número que ingresastes fue {numero}")
