# Task management

import os

task_list: list[str] = []

def limpiar_consola() -> None:
    # nt => windows | os.name => detecta el sistema operativo
    # os.system() => ejecuta comandos del o.s actual

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu() -> str:
    menu = """ TASK MANAGEMENT
    \n 1. Listar tareas
    \n 2. Agregar tarea
    \n 3. Editar tarea
    \n 4. Eliminar tarea
    \n 5. Limpiar lista de tareas
    \n 6. Salir
"""

    return menu

def listar_tareas() -> None:
    # Si la lista no esta vacía : len!=0 = True
    if len(task_list):
        # con enumerate : obtener posicion, elemento
        for i, task in enumerate(task_list):
            print(f"{int(i) + 1} - {task}")
    else:
        print("No hay tareas registradas actualmente")

def agregar_tarea(task: str) -> None:
    # Función para agregar una nueva tarea a la lista
    task_list.append(task)

def editar_tarea(id: int) -> None:
    # Función para editar una tarea previamente registrada
    mensaje : str = "No hay tareas registradas actualmente"

    # Si la lista no esta vacía
    if len(task_list):
        # Si existe el id ingresado (edita), sino ejecuta sentencia else
        if 0 <= id - 1 < len(task_list):
            # Función para editar la info de una tarea registrada previamente
            task_list[id - 1] = input("Ingrese el nombre editado de la tarea: \n")
            mensaje : str = "Tarea editada exitosamente"
        else:
            mensaje : str = "Tarea no encontrada"

    return mensaje

def eliminar_tarea(id: int) -> str:
    mensaje : str = "No hay tareas registradas actualmente"

    # Función para eliminar una tarea
    if len(task_list):
        if 0 <= id - 1 < len(task_list):
            task_list.pop(id - 1)
            mensaje : str = "Tarea eliminada exitosamente"
        else: 
            mensaje : str = "Tarea no encontrada"

    return mensaje

def limpiar_lista() -> None:
    # Función para eliminar todas las tareas
    task_list.clear()

# variable usada para condicionar si se muestra menú principal 
# y se realizan operaciones o no
response = True

while True:

    if response:

        limpiar_consola()

        print(menu())
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print("Tareas")
            listar_tareas()
        elif opcion == "2":
            task: str = input("Ingrese nombre de la tarea:\n")
            agregar_tarea(task)
            print("Tarea registrada exitosamente")
        elif opcion == "3":
            id = int(input("Ingrese id de la tarea a editar: \n"))
            print(editar_tarea(id))
        elif opcion == "4":
            id = int(input("Ingrese id de la tarea a eliminar: "))
            print(eliminar_tarea(id))
        elif opcion == "5":
            limpiar_lista()
            print("Lista de tareas eliminada exitosamente")
        elif opcion == "6":
            print("Gracias por usar el programa")
            break
    else:
        print("Gracias por usar el programa")
        break
    
    # operación lógica retorna bool 
    response = input("¿Desea regresar al menú principal? (S/N): ").lower() == "s" 
