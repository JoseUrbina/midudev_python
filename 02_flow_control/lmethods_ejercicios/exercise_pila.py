# Simulador del funcionamiento de una pila (usando listas)

import os
os.system("clear" if os.name == "posix" else "cls")

pila = []

# Menú de opciones
def opciones():
    print("-"*15)
    return int(input(f'''\nBienvenido a nuestra pila. Opciones:
    1. Ingresar nuevo elemento
    2. Ver todos los elementos
    3. Eliminar elemento
    4. Salir
'''))

def agregar_elemento(e: str) -> None:
    # Función que permite agregar un elemento nuevo a la PILA
    pila.append(e)

def mostrar_elementos() -> None:
    # Función para mostrar todos los elementos de la PILA
    print(f"PILA: {pila}")

def eliminar_elemento() -> str:
    # Función para eliminar un elemento de la pila
    return pila.pop()

while True:
    opcion = opciones()
    valido = True

    match opcion:
        case 1:
            elemento = input("Ingrese el nombre del elemento:")
            agregar_elemento(elemento)
        case 2:
                mostrar_elementos()
        case 3:
            if len(pila) == 0:
                print("PILA vacía. Favor ingrese un nuevo elemento.")
            else:
                elemento = eliminar_elemento()
                print(f"El elemento [{elemento}] de la PILA fue eliminado correctamente.")
        case 4:
            print("Gracias por su participación, regrese pronto.")
            break
        case _:
            valido = False
            print("Opción no válida, intente de nuevo.")

    if valido:
        print(f"La PILA tiene {len(pila)} elementos.")
