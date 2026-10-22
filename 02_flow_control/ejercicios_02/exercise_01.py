# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

import os

os.system("clear" if os.name == "posix" else "cls")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El primer número es mayor")
elif numero2 > numero1:
    print("El segundo número es mayor")
else:
    print("Ambos números son iguales")
