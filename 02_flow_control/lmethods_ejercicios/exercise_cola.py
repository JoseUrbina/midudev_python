# Simulador de estructura de datos COLA

import os
os.system("clear" if os.name == "posix" else "cls")

cola = []

def opciones() -> None:
    # función para mostrar las opciones permitadas en el programas.
    print("-" * 60)
    return int(input((f'''\nBienvenido a nuesta estructura de cola. Opciones:
        1. Agregar nuevo elemento
        2. Mostrar todos los elementos
        3. Eliminar elemento
        4. Salir
    ''')))

def agregar_elemento(elemento: str) -> None:
    # Función para agregar un elemento nuevo a la estructura de cola.
    cola.append(elemento)

def mostrar_elementos():
    # Función para mostrar todos los elementos de la cola.
    print(f"Cola = {cola}")

def eliminar_elemento() -> str:
    # Función que permite eliminar elemento de la cola.
    return cola.pop(0)

while True:

    opcion = opciones()
    valido = True

    match opcion:
        case 1:
            elemento = input("Ingrese un nuevo elemento: ")
            agregar_elemento(elemento)
            print("Elemento agregado correctamente.")
        case 2:
            mostrar_elementos()
        case 3:
            if len(cola) == 0:
                print("COLA vacía, favor agregar elementos.")
            else:
                elemento = eliminar_elemento()
                print(f" Elemento [{elemento}] eliminado correctamente.")
        case 4:
            print("Gracias por su participación, tenga buen día.")
            break
        case _:
            valido = False
            print("Opción no permitida, favor volver a intentarlo.")

    if valido:
        print(f"La COLA tiene {len(cola)} elementos.")
