
import os

os.system("clear" if os.name == "posix" else "cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

print(f"{'-'*10}")

nombre = input("Ingresa tu nombre: ")
ciudad = input("Ingresa tu ciudad: ")

print("\nTu nombre es:", nombre)
print("Tu ciudad es:", ciudad)

print(f"{'-'*10}")
