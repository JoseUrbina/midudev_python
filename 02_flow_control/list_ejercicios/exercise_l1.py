# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

import os
os.system("clear" if os.name == "posix" else "cls")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

lista = [] # new list

lista += mensaje[-7:] # slicing and concatenating
# lista += mensaje[7:] # other way to do it

print(f"New list: {lista}") # showing new list
