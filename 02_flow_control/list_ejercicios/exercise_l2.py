# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

import os
os.system("clear" if os.name == "posix" else "cls")

numeros = [10, 20, 30, 40, 50]

### Manera tradicional de hacer ###

# primera_posicion = numeros[0]
# numeros[0] = numeros[-1]
# numeros[-1] = primera_posicion

numeros[0], numeros[-1] = numeros[-1], numeros[0] # en una sola línea

# a = 10
# b = 50

# a , b = b, a
# print(a, b)

print(f"Valores intecambiados: {numeros}")
