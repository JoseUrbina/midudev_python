# Practice 1 - Dictionary

import os

inventario = {
    "manzanas": 10,
    "papanas": 5,
    "leche": 8
}

def limpiar_pantalla() -> None:
    os.system("clear" if os.name == "posix" else "cls")

def menu_interactivo() -> None:
    print("--- Sistema de Control de Inventario ---")
    print("1. Agregar o actualizar stock")
    print("2. Consultar inventario")
    print("3. Salir\n")

while True:
    limpiar_pantalla()
    menu_interactivo()

    opcion = int(input("Selecciona una opción (1-3): ").strip())

    match opcion:
        case 1: 
            producto = input("¿Ingrese el nombre del producto?: ").strip().lower()

            try:
                cantidad = int(input("¿Cantidad del producto ha añadir?: "))

                # .get(producto, 0) : devuelve 0 si el producto aún no existe en el diccionario
                inventario[producto] = inventario.get(producto, 0) + cantidad
                print(f"Se actualizarón las existencias de '{producto}'. Total: {inventario[producto]}")
            except ValueError:
                print("Error: Debes ingresar un número entero válido para la cantidad")
        case 2: 
            print("\n--- Inventario actual ---")
            if not inventario:
                print("El inventario esta vacío.")
            else:
                for producto, cantidad in inventario.items():
                    print(f"{producto.capitalize()} : {cantidad} unidades")
        case 3: 
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")

    input("\nPresiona Enter para continuar...")
