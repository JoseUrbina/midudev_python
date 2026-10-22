# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero

    numero += 1

print(f"Sumatoria de los número pares entre 1-20: {suma}")
