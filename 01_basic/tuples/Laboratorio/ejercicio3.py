"""
Usando la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
genera una tupla llamada pares. Imprime dicha tupla en consola.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = tuple([n for n in my_list if n % 2 == 0])

print(pares)
