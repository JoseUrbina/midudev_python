# Ejercicio 1: Añadir y modificar elementos

import os
os.system("clear" if os.name == "posix" else "cls")

# Crea una lista con los números del 1 al 5.
lista = [1, 2, 3, 4, 5]
print(lista)

# Añade el número 6 al final usando append().
lista.append(6)
print(lista)

# Inserta el número 10 en la posición 2 usando insert().
lista.insert(2, 10)
print(lista)

# Modifica el primer elemento de la lista para que sea 0.
lista[0] = 0
print(lista)
