###
# Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os

os.system("clear" if os.name == "posix" else "cls")

print("Sentecia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

print("\nSentencia condicional con else")

edad = 17

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")

print("\nSentencia condicional con elif")

nota = 7

# Porque solo >= ; porque en el condicional if si se cumple una condición, el resto se omite.
# else: no es obligatorio.

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("No estas calificado")

print("\n Condiciones múltiples")

edad = 16
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
else:
    print("POLICIA!!!")

# un pueblo de isla margarita

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Margarita")
else:
    print("Paga al policía y te deja conducir en la Isla Margarita")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("Es un día laborable, a trabajar!")

print("\n Anidar condicionales")

edad = 20
tiene_dinero = False

if edad >= 18:
    if tiene_dinero:
        print("Puedes salir a divertirte")
    else:
        print("Quedate en casa")
else:
    print("No puedes salir a divertirte")

edad = 19
tiene_dinero = True

# Versión corta
if edad < 18:
    print("No puedes salir a divertirte")
elif tiene_dinero:
    print("Puedes salir a divertirte")
else:
    print("Quedate en casa")

# Valores evaludados como booleanos en condiciones

print("\nValores evaludados como booleanos en condiciones")
numero = 3
if numero: # True
    print("EL número no es cero")

numero = 0
if numero: # False
    print("No va a entrar nunca.")

nombre = "José"
if nombre: #True
    print("El nombre no esta vacío")

nombre = ""
if nombre: #False
    print("No va a entrar nunca")

# Operadores de comparación usado para cadena
print("\nCompación de cadenas")
# la compación ira letra por letra hasta encontrar una que cumpla la condición
print(f"manzana < pera: {'manzana' < 'mera'}")

print("\nCondición ternaria")

edad = 16
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
