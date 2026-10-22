"""
Crea una lista de longitud 5 que contengan tuplas 
de 2 elementos de números enteros. (e.g (10, 20) ) . 
Utilizando un ciclo for-each, imprime en consola las tuplas. 
Cada impresión en consola (Una por cada elemento) debe 
seguir el siguiente formato: ‘{first_element} - {second_element}’. 
La lista debe tener por nombre: my_list
"""

my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for tupla in my_list:
    first_element, second_element = tupla

    print(f"{first_element}  - {second_element}")
