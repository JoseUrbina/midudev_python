###
# 04 - List Methods
# Los métodos más importantes para trabajar con listas
###

import os
os.system("clear" if os.name == "posix" else "cls")

lista1 = ['a', 'b', 'c', 'd', '@']

### Añadir o insertar elementos a la lista

lista1.append('e') # Agrega un elemento al final de la lista
print(f".append(e): {lista1}")

lista1.extend(['i', 'f', 'h']) # Agrega un conjunto de elementos
print(f".extend([x, x...]): {lista1}")

lista1.insert(1, '@') # agrega un elemento en una posición especifica de la lista
print(f".insert(i,e): {lista1}")

### Eliminar elementos de la lista

lista1.remove('@') # Elimina la primera aparición del elemento en la lista
print(f".remove() : {lista1}")

resultado = lista1.pop() # Elimina el ultimo elemento de la lista por defecto
print(f".pop(): {resultado}")

# .pop() se puede pasar un indice para eliminar un elemento especifico
eliminado = lista1.pop(2)
print(f".pop(i): {eliminado}")

# del :elimina un elemento o por rangos

del lista1[-1]
print(f"del: {lista1}")

del lista1[2:4] # eliminación de rangos de valores
print(f"del [rango]: {lista1}")

# .clear() => eliminar todos los elementos de la lista
lista1.clear()
print(f".clear(): {lista1}")

# Ordenar elementos de la lista

print("\nOrdenar listas en su original")
numbers = [3, 10, 2, 8, 99, 101]
print(f"Original: {numbers}")
numbers.sort()
print(f".sort() : {numbers}")

print("Ordenar listas creando una nueva")
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(f"Original: {numbers} | sorted(): {sorted_numbers}")

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ["manzana", "pera", "limón", "manzana", "pera", "limón"]
sorted_frutas = sorted(frutas)
print(f"Lista en minusculas ordenada: {sorted_frutas}")

print("Ordenar una lista de cadenas de texto (mezclas mayusculas y minusculas)")
frutas = ["manzana", "pera", "Limón", "manzana", "pera", "limón"]
frutas.sort(key=str.lower) # comparación por minusculas
print(f"Lista ordenada sin distinción: {frutas}")

# más metodos utiles

numbers = [3, 10, 2, 8, 99, 3, 101]
print(len(numbers)) # cantidad de elementos de la lista
print(numbers.count(3)) # cantidad de veces que aparece un elementos

print(10 in numbers) # verificar si el elemento esta en la lista
print(5 in numbers) # false
