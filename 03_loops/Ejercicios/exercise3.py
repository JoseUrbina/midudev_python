# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. 
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

try:
    numero = int(input("¿Ingrese un número entero positivo?"))

    if numero < 0:
        print("Valor no válido, debes ingresar un número entero positivo.")
    else:
        contador = 1
        factorial = contador

        while contador < numero:
            contador += 1
            factorial *= contador

        print(f"Factorial (5): {factorial}")
except ValueError:
    print("Valor no válido, debes ingresar un número entero positivo.")
