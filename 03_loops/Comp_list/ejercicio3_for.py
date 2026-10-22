# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]

maximo = 0

for numero in numeros:
    if maximo < numero:
        maximo = numero

print(f"Número máximo: {maximo}")
