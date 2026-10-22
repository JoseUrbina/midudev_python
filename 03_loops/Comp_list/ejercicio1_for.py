# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for numero in range(2, 20 + 1):
    if numero % 2 == 0:
        print(numero)

pares = [numero for numero in range(2, 20 + 1) if numero % 2 == 0]
print(pares)