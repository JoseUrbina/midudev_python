# Listas: Ocultar parte de un número de teléfono

import os
os.system("clear" if os.name == "posix" else "cls")

telefono = input("¿Cúal es tu telefono (8 caracteres)?: ")

print(f"Telefono codificado: ****{telefono[-4:]}")
