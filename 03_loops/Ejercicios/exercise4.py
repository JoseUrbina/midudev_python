# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    contra = input("\nIngrese una contraseña: ")

    if len(contra) >= 8:
        print("\nContraseña válida")
        break
    else:
        print("\nContraseña inválida, debe tener al menos 8 caracteres.")
