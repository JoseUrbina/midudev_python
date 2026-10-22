# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

import os
os.system("clear" if os.name == "posix" else "cls")

lista = [1, 2, 3]
new_lista = lista * 2

print("Lista original -> Lista con duplicados")
print(f"{lista} -> {new_lista}")
