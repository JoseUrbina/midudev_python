import os
os.system("clear" if os.name == "posix" else "cls")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
original = [1, 2, 3]
print(f"Original: {original}")

# Crea una copia de la lista original llamada copia_1 usando slicing.
copia_1 = original[:]
print(f"Original: {original} | copia 1: {copia_1}")

# Crea otra copia llamada copia_2 usando copy().
copia_2 = original.copy()
print(f"Original: {original} | copia 2: {copia_2}")

# Crea una referencia a la lista original llamada referencia.
referencia = original
print(f"Original: {original} | referencia: {referencia}")

# Modifica el primer elemento de la lista referencia a 10.
referencia[0] = 10
print(f"Original: {original} | referencia: {referencia}")

# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print(f"\n{" - "*15}\n")
print(f"Original: {original}")
print(f"copia 1: {copia_1}")
print(f"copia 2: {copia_2}")
print(f"referencia: {referencia}") 
