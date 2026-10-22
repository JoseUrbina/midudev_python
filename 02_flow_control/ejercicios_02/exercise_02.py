# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

import os

os.system("clear" if os.name == "posix" else "cls")

def suma(num1: float, num2: float) -> float:
    return num1 + num2

def resta(num1: float, num2: float) -> float:
    return num1 - num2

def multiplicacion(num1: float, num2: float) -> float:
    return num1 * num2

def division(num1: float, num2: float) -> float:
    return num1 / num2

numero1: float = float(input("Ingrese el 1er número: "))
numero2: float = float(input("Ingrese el 2do número: "))
operacion: str = input("Operación (+, -, *, /): ")

resultado: float = 0

# variable usada para verificar que ocurrio error en / operación
error = False

if operacion == "+":
    resultado = suma(numero1, numero2)
elif operacion == "-":
    resultado = resta(numero1, numero2)
elif operacion == "*":
    resultado = multiplicacion(numero1, numero2)
elif operacion == "/":
    if numero2 == 0:
        print("ERROR: zero division error.")
        error = True
    else:
        resultado = division(numero1, numero2)

# Si no hay ningún error: execute order
if not error:
    print(f"El resultado de la operacion de {operacion} es {resultado}")
