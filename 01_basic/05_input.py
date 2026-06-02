###
# 05 - entrada de usuario (input()) - Versión simplicada
# La función input() permite obtener datos del
# usuario a traves de la consola
###

# print("Hola, como te llamas?")
# nombre = input()

# print(f"Bienvenido, {nombre}. Encantado de conocerte.")

nombre = input("Hola, como te llamas?\n")
print(f"Bienvenido, {nombre}. Encantado de conocerte.")

# SIEMPRE todo datos que se obtenga del input() será un str
age = input("Cuantos años tienes?\n")

print(type(age))

age = int(age)

print(type(age))

print(f"Dentro de 20 años tendrás {age + 20} años.")


print("Obtener múltiples valores a la vez")

# split() : valor separador por defecto es ( ), toma la cadena entera
# y la divide por ( ), retornando una lista

country, city = input("¿En que país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")

number1, number2, number3 = [1, 3, 4]

print(number1, number2, number3)
