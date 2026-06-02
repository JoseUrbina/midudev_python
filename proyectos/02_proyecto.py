# Calculadora básica con operación en notación cientifica

import os
import time

def mostrar_menu():
    print("\n Calculador Cientifica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def o_suma(num1: float, num2: float) -> float:
    return num1 + num2

def o_resta(num1:float , num2:float) -> float:
    return num1 - num2

def o_multiplicacion(num1: float, num2: float) -> float:
    return num1 * num2

def o_division(num1: float, num2: float) -> float:
    return num1 / num2

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    if opcion not in ['1', '2', '3', '4', '5']:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
        r = input("¿Desea continuar con otra operación (S/N)?: ").lower() == "s"

        # if not true: retorna False, sale del programa
        if not r:
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        # True: retorna al menú principal
        continue

    numero1 = float(input("Ingrese el primer número (1e3): "))
    numero2 = float(input("Ingrese el segundo número (2.5e-2): "))

    if opcion == '1':
        resultado = o_suma(numero1, numero2)
        print(f"El resultado de la suma es {resultado:.2e}")
    elif opcion == '2':
        resultado = o_resta(numero1, numero2)
        print(f"EL resultado de la resta es {resultado:.2e}")
    elif opcion == '3':
        resultado = o_multiplicacion(numero1, numero2)
        print(f"El resultado de la multiplicación es {resultado:.2e}")
    elif opcion == '4':
        if numero2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = o_division(numero1, numero2)
            print(f"El resultado de la división es {resultado:.2e}")

    r = input("¿Desea continuar con otra operación (S/N)?: ").lower() == "s"

    if not r:
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    # True: retorna al menú principal
    continue
