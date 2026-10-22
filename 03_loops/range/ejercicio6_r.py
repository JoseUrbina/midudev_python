# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

numero = int(input("Ingrese un número: "))

print(f"\nTabla de multiplicar del {numero}")

for n in range(1, 10 + 1):
    print(f"{numero} * {n} = {numero * n}")
