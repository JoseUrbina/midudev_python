###
# 02_types.py
# Python tiene varios tipos de datos
# int, float, str, complex, bool, list, tuple, range, NoneType, set ...
###

# Comentario de una sola linea

"""
    Esta es una cadena de texto
    multilinea, y si no se asigna a nada,
    se considera un comentario de varias lineas (docstring)
"""

print("int: ")
print(type(10))
print(type(0))
print(type(-5))

# python : puede manejar enteros de gran tamaño sin problemas
print(type(1232525235263463463263463434634646))
print(12325252352634634632634634346346463453234234132 + 1)

print("float: ") 
print(type(3.1416))
print(type(1.0))

# Siempre que se utiliza notación cientifica, es tomado como float
print(type(1e3)) # notación científica 1000.0

print("complex: ")
print(type(1 + 2j))

print("str: ")
print(type("Hola, mundo!"))
print(type("123"))
print(type(""))
print(type("""
    Esto es una cadena de texto multilinea
"""))

print("bool: ")
print(type(True))
print(type(False))

# operaciones logicas : resultado valores booleanos (True or False)
print(type(1 > 2))

# None => ausencia de valor
print("Nonetype:")
print(type(None))
