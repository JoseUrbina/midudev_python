# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

import os
import math

os.system("clear" if os.name == "posix" else "cls")

lista = [10, 20, 30, 40, 50]

###  posicion: almacena posición del centro de la lista  ###
# -1 -> len: inicia a contar en 1 para obtener total de elementos, 
# lo que necesitamos hacer para obtener el indice exacto se le resta 1
# retorna el resultado de la división en entero (convierte el resultado de la división normal) : //

# posicion = (len(lista) - 1) // 2

# posicion + 1: para solo recorrer 1 posición
### Python evalua la expresión de izd -> der (1ero obtiene la lista y despues del resultado se obtiene el valor)
# elemento = lista[posicion:posicion+1][0]

# Sin utilizar slicing
posicion = len(lista) // 2

print(f"El centro es {lista[posicion]}")
