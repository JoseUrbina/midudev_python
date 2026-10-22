# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

import os

os.system("clear" if os.name == "posix" else "cls")

edad = int(input("Ingrese una edad: "))

if edad >= 65:
    print("Adulto Mayor")
elif edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("Adolescente")
elif edad >= 3:
    print("Niño")
elif edad >= 0:
    print("Bebé")
else:
    print("Edad inválida")
