# Mini ejercicio para practicar listas

import os
os.system("clear" if os.name == "posix" else "cls")

datos = [5, 10, 15, 20, 25, 30, 35, 40]

# 1. Obtenga los primeros 4 elementos
print(f"Primeros 4 elementos: {datos[0:4]}")

# 2. Obtenga los últimos 3 elementos

print(f"Últimos 3 elementos: {datos[5:]}") # 1er forma
print(f"Últimos 3 elementos: {datos[-3:]}") # 2da forma

# 3. Obtenga los elementos en posiciones pares

print(f"Elementos en posiciones pares: {datos[::2]}")

# 4. Obtenga la lista invertida

print(f"Original: {datos} || Invertida: {datos[::-1]}")

# 5. Obtenga los elementos desde el índice 2 hasta el 5

print(f"Elementos del 2 al 5: {datos[2:6]}")

# 6. Obtener los elementos en posiciones impares

print(f"Elementos en posiciones impares: {datos[1::2]}")
