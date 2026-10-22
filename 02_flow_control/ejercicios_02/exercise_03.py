# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

import os

os.system("clear" if os.name == "posix" else "cls")

def es_bisiesto(anio: int) -> bool:
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

anio = int(input("Ingrese el año: "))

if es_bisiesto(anio):
    print("Es año bisiesto")
else:
    print("No es año bisiesto")
