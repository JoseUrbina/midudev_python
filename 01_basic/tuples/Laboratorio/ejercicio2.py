"""
Define una tupla de longitud 5 (Cualquier tipo de dato)
y usando tuple unpacking genera 3 nuevas variables para, 
el primer , penúltimo y el último elemento. 
Imprime dichas variables en consola. 
La tupla debe tener por nombre my_tuple.
"""

my_tuple = (None, 20, 30, None, None)

primero, *_, penultimo, ultimo = my_tuple

print(primero)
print(penultimo)
print(ultimo)
