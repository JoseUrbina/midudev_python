# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

suma = 0

for n in range(1, 100 + 1):
    suma += n

print(f"La suma de los números entre 1 - 100 es: {suma}")
