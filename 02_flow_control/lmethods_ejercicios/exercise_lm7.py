# verificar si la str contiene vocales

import os
os.system("clear" if os.name == "posix" else "cls")

print("Verificador si existen vocales en el texto")
frase = input("Escriba lo que desee: ")

encontrado = False

for letra in frase:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        encontrado = True
        break

print(f"El texto [{frase}] {'contiene vocales' if encontrado else 'no contiene vocales'}")
