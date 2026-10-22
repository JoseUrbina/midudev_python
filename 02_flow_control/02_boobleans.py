###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso)
# Fundamentales para el control de flujo y la lógica de programación
###

# Los booleanos representan valores de verdad: True and False

print("\nValores boobleanos básicos")
print(True)
print(False)

# Operadores de comparación: devuelven un valor boobleano
print("\nOperadores de comparación")
print(f"5 > 3: {5 > 3}") # True
print(f"5 < 3: {5 < 3}") # False
print(f"5 == 5: {5 == 5}") # True (igualdad)
print(f"5 != 3: {5 != 3}") # True (desigualdad)
print(f"5 >= 5: {5 >= 5}") # True (mayor o igual que)
print(f"5 <= 3: {5 <= 3}") # True (menor o igual que)

# Operadores lógicos: and, or, not
print("\nOperadores lógicos")
print(f"True and True: {True and True}") # True
print(f"True and False: {True and False}") # False
print(f"True or True: {True or True}") # True
print(f"True or False: {True or False}") # True
print(f"False or False: {False or False}") # False
print(f"not True: {not True}") # False
print(f"not False: {not False}") # True

# Tablas de verdad para referencia
print("\nTablas de verdad")
print("AND")
print("A        B       A and B")
print(f"True     True    {True and True}")
print(f"True     False   {True and False}")
print(f"False    True    {False and True}")
print(f"False    False   {False and False}")

print("\nOR")
print("A        B       A or B")
print(f"True     True    {True or True}")
print(f"True     False   {True or False}")
print(f"False    True    {False or True}")
print(f"False    False   {False or False}")

print("\nNOT")
print("A        not A")
print(f"True     {not True}")
print(f"False    {not False}")
