import os
os.system("clear" if os.name == "posix" else "cls")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista: {lista}")

# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
del lista[2:5]

# Imprime la lista resultante.
print(f"Lista resultante: {lista}")
