###
# 03 - Listas
# Secuencias mutables de elementos. 
# Pueden contener elementos de diferentes tipos.
###

import os
os.system("clear" if os.name == "posix" else "cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = list([1, 2, 3, 4])

lista3 = ["manzana", "banana", "pera"] # lista de cadenas
lista4 = [1, "hola", 3.14, True] # lista de elementos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ["calcetin", 4]]
matrix = [[1, 2], [3, 4], [5, 6]]

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

print(lista_de_listas[1][0])

# Acceso a elementos por índice

# izq a der : 0, 1, ...
# der a izq : -1, -2, ...

print("\nAcceso a elementos por índice")
print(lista3[0]) # manzanas
print(lista3[1]) # banana
print(lista3[-1]) # pera : acceso a elementos por índices negativos
print(lista3[-2]) # banana
print(lista_de_listas[1][0]) # [] -> de afuera hacia adentro

# slicing (rebanado) de listas

print("\nSlicing listas")

lista1 = [1, 2, 3, 4, 5]

# [desde:hasta:paso] : desde: indice de inicio, hasta: indice final sin incluir, paso: pasos a hacer

print(lista1[1:4])

print(lista1[:3])

print(lista1[:]) # copia de la lista

# HAY MÁS MAGIA

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Indices pares: {lista1[::2]}")
print(f"Original: {lista1} | Invertida: {lista1[::-1]}")

### Modificar una lista ###

# Acceder a posición de lista: nombre_lista[indice]
# Modificar valor : nombre_lista[indice] = new_value

lista1[0] = 20
print(lista1)

### Añadiendo elementos a la lista

lista1 = [1, 2, 3]

print(f"Lista original: {lista1}")

# forma larga, menos eficiente
lista1 = lista1 + [4, 5, 6]

print(lista1)

# forma corta, más eficiente
lista1 += [7, 8 ,9]

print(lista1)

### Longitud de una lista

print(len(lista1))
