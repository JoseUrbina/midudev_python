# Crear una copia de una lista

import os
os.system("clear" if os.name == "posix" else "cls")

original = [1, 2, 3, 4]

# copia identica, diferente dirección de memoria
copia = original[:]

copia += [5, 6, 7]

print(f"Original: {original} | Copia: {copia}")
