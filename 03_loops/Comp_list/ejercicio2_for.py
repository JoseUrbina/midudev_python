# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]

# forma 1
suma = 0
promedio = 0

for numero in numeros:
    suma += numero
else:
    promedio = suma / len(numeros)

print(f"Media: {promedio}")

# forma 2

promedio = sum(numeros) / len(numeros)
print(f"Media: {promedio}")
