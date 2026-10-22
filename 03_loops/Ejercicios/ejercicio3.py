import os

estudiantes: dict = {}

def limpiar_pantalla() -> None:
    os.system("clear" if os.name == "posix" else "cls")

def menu_principal() -> None:
    print("--- Registro de calificaciones y promedio ---")
    print("1. Registrar estudiante y agregar nota")
    print("2. Ver reporte de estudiantes")
    print("3. Salir")

while True:
    limpiar_pantalla()
    menu_principal()

    opcion = int(input("Seleccione una opción (1-3): ").strip())

    match opcion:
        case 1:
            print("\nRegistro de estudiante y su nota")
            nombre = input("Ingrese el nombre del estudiante: ").strip()

            try:
                nota = int(input("Ingrese la nota (0-100): "))

                if 0 <= nota <= 100:
                    estudiantes.setdefault(nombre, []).append(nota)

                    print(f"Al estudiante {nombre} se le agregó la nota de {nota}.")
                else:
                    print("Nota no válida, el rango permitido es entre 0 - 100")
            except ValueError:
                print("Valor no válido. Ingrese un valor númerico entre 0-100")
        case 2:
            if not estudiantes:
                print("No hay estudiantes registrados actualmente.")
            else:
                for estudiante, notas in estudiantes.items():
                    print(f"{estudiante} | Notas: {notas} | Promedio final: {sum(notas)/len(notas)}")
        case 3:
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        case _:
            print("\nOpción no válida. Favor intentar de nuevo.")

    input("\nPresione Enter para continuar...")
