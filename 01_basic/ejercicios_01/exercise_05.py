
import os
import math

os.system("clear" if os.name == "posix" else "cls")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print(f"{'-'*10}")

# Redondeamos directamente el valor de pi sin almacenarlo en una variable

print(f"Valor de PI: {math.pi}")

print(f"PI redondeado: {round(math.pi)}")

division_entera = round(math.pi) // 2

print(f"División entera de PI redondeado entre 2: {division_entera}")

print(f"{'-'*10}")
