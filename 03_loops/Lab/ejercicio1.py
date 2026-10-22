"""
    Crea una lista de longitud 10. 
    Utilizando un ciclo for-each imprime en 
    consola todos los números pares mayores a 5. 
    La lista debe tener por nombre my_list.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in my_list:
    if (numero % 2 == 0) and numero > 5:
        print(numero)
