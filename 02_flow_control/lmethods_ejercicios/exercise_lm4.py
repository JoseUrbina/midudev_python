import os
os.system("clear" if os.name == "posix" else "cls")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
lista = [5, 2, 8, 1, 9, 4, 2]
print(f"Lista: {lista}")

# Ordena la lista de forma ascendente usando sort().
lista.sort()
print(f"Lista ordenada de forma ascedente: {lista}")

# Cuenta cuántas veces aparece el número 2 en la lista usando count().

contador = lista.count(2)
print(f"Cantidad de veces que aparece el número 2: {contador}")

# Comprueba si el número 7 está en la lista usando in.
esta_en_lista = 7 in lista
print(f"¿El número 7 está en la lista? : {"si" if esta_en_lista else "no"}")
