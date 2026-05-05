###
# 03 casting de types
# Transformar un tipo de un valor a otro
# Python: no realiza converción de tipos de manera automatica. (tipado fuerte)
###

print("*** Conversión de tipos ***")
print(type("100"))
print(type(int("100")))

# Si no se realiza la conversión, genera error en ambos casos
print("100" + str(2))
print(2 + int(100))

print(type(float("3.1416")))

# bool: 0 es el único valor numerico que es false
print(bool(3))
print(bool(0))
print(bool(-1))

# converter: number to bool
num = int(input("Ingrese un número: "))

valor_booleano = bool(num)
print(valor_booleano)

# bool: solo el string "" vacío es False, string con contenido : True

print(bool(""))
print(bool(" "))
print(bool("False"))

# function round(value) : si el valor es .5 (en medio) redondea al par más cercano

print(round(2.5))  # r:2
print(round(3.5))  # r:4
print(round(2.4))  # r:2
print(round(2.51)) # r:3
