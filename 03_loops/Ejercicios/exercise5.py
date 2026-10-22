# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Ingrese un número: "))
i = 1

print(f"\nTabla de multiplicar del número ({numero})")
while i <= 10:
    print(f"{numero} x {i} = {numero*i}")
    i += 1
