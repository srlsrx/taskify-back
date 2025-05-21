from controllers.task_controller import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    get_tasks_by_user,
)

import utils.session
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_admin_tasks_menu():
    while True:
        limpiar_consola()
        print("=== MENÚ TO-DO LIST ===")
        print("1. Crear tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tarea por ID")
        print("4. Ver tareas por usuario")
        print("5. Actualizar tarea")
        print("6. Eliminar tarea")
        print("7. Salir")
        print("=========================")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            create_task_menu()
        elif choice == "2":
            get_all_tasks_menu()
        elif choice == "3":
            get_task_by_id_menu()
        elif choice == "4":
            get_tasks_by_user_menu()
        elif choice == "5":
            update_task_menu()
        elif choice == "6":
            delete_task_menu()
        elif choice == "7":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def display_users_tasks_menu():
    print(utils.session.current_user.id)
    while True:
        limpiar_consola()
        print("=== MENÚ TO-DO LIST ===")
        print("1. Crear tarea")
        print("2. Ver mis tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("=========================")
        choice = input("Selecciona una opción (1-5):")
        if choice == "1":
            limpiar_consola()
            create_task_menu()
        elif choice == "2":
            limpiar_consola()
            tasks = get_tasks_by_user(utils.session.current_user.id)
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tienes tareas asignadas")
            input("Pulsa cualquier tecla para continuar...")
        elif choice == "3":
            limpiar_consola()
            update_task_menu()
        elif choice == "4":
            limpiar_consola()
            delete_task_menu()
        elif choice == "5":
            break
        else:
            print("Opcion no valida")


def create_task_menu():
    print("=== CREAR TAREA ===")
    if utils.session.current_user.is_admin:
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la descripción de la tarea: ")
        id = int(input("Ingrese el ID del usuario: "))
        task = create_task(name, description, id)
    else:
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la descripción de la tarea: ")
        task = create_task(name, description, utils.session.current_user.id)
    if task:
        print(f"Tarea creada: {task}")
    else:
        print("Tarea no creada")
    input("Pulsa cualquier tecla para continuar...")
    print("=====================")


def get_all_tasks_menu():
    print("=== TODAS LAS TAREAS ===")
    tasks = get_all_tasks()
    if tasks:
        for task in tasks:
            print(task)
    print("===============================")
    input("Pulsa cualquier tecla para continuar...")


def get_task_by_id_menu():
    print("=== CONSULTAR TAREA POR ID ===")
    task_id = int(input("Ingrese el ID de la tarea: "))
    task = get_task_by_id(task_id)
    if task:
        print(task)
    print("===============================")
    input("Pulsa cualquier tecla para continuar...")


def get_tasks_by_user_menu():
    print("=== CONSULTAR TAREAS POR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario: "))
    tasks = get_tasks_by_user(user_id)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No se encontraron tareas para este usuario.")
    print("===============================")
    input("Pulsa cualquier tecla para continuar...")


def update_task_menu():
    print("=== ACTUALIZAR TAREA ===")
    task_id = int(input("Ingrese el ID de la tarea a actualizar: "))
    name = input("Ingrese el nuevo nombre de la tarea (dejar vacío para no cambiar): ")
    description = input(
        "Ingrese la nueva descripción de la tarea (dejar vacío para no cambiar): "
    )
    is_done = input("¿La tarea está completada? (s/n): ").lower()
    if is_done == "s":
        is_done = True
    elif is_done == "n":
        is_done = False
    else:
        print("Opción no válida. La tarea no se actualizará.")
        return
    task = update_task(task_id, name, description, is_done)
    if task:
        print(f"Tarea actualizada: {task}")
    else:
        print("Tarea no encontrada.")
    print("===============================")
    input("Pulsa cualquier tecla para continuar...")


def delete_task_menu():
    print("=== ELIMINAR TAREA ===")
    task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    task = delete_task(task_id)
    if task:
        print(f"Tarea eliminada: {task}")
    print("===============================")
    input("Pulsa cualquier tecla para continuar...")


if utils.session.current_user:
    if utils.session.current_user.is_admin:
        display_admin_tasks_menu()
    else:
        display_users_tasks_menu()
