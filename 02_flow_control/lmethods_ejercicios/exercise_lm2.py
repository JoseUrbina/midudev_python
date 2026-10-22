# Ejercicio 2: Combinar y limpiar listas

import os
os.system("clear" if os.name == "posix" else "cls")

# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

print(f"Lista a: {lista_a} | Lista b: {lista_b}")

# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print(f"Lista a: {lista_a} | Lista b: {lista_b}")

# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
print(f"Lista_a sin el número 1: {lista_a}")

# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
pop_element = lista_a.pop(3)
print(f"Elemento eliminado en el indice 3 de lista_a: {pop_element}")

# Limpia completamente lista_b usando clear().
lista_b.clear()
print(f"Lista a: {lista_a} | Lista b: {lista_b}")
