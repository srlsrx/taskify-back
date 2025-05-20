# --- MENÚ TO-DO LIST ---
# 1. Crear tarea
# 2. Ver todas las tareas
# 3. Ver tarea por ID
# 4. Actualizar tarea
# 5. Eliminar tarea
# 6. Salir

from controllers.task_controller import (create_task, delete_task, get_all_tasks, get_task_by_id, update_task, get_tasks_by_user)
from models.task_model import Task
from models.user_model import User

def display_menu():
    while True:
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
        if choice == '1':
            create_task_menu()
        elif choice == '2':
            get_all_tasks_menu()
        elif choice == '3':
            get_task_by_id_menu()
        elif choice == '4':
            get_tasks_by_user_menu()
        elif choice == '5':
            update_task_menu()
        elif choice == '6':
            delete_task_menu()
        elif choice == '7':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def create_task_menu():
    print("=== CREAR TAREA ===")
    name = input("Ingrese el nombre de la tarea: ")
    description = input("Ingrese la descripción de la tarea: ")
    user_id = int(input("Ingrese el ID del usuario: "))
    task = create_task(name, description, user_id)
    print(f"Tarea creada: {task}")
    print("=====================")

def get_all_tasks_menu():
    print("=== TODAS LAS TAREAS ===")
    tasks = get_all_tasks()
    for task in tasks:
        print(task)
    print("===============================")

def get_task_by_id_menu():
    print("=== CONSULTAR TAREA POR ID ===")
    task_id = int(input("Ingrese el ID de la tarea: "))
    task = get_task_by_id(task_id)
    if task:
        print(f"Tarea encontrada: {task}")
    else:
        print("Tarea no encontrada.")
    print("===============================")

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

def update_task_menu():
    print("=== ACTUALIZAR TAREA ===")
    task_id = int(input("Ingrese el ID de la tarea a actualizar: "))
    name = input("Ingrese el nuevo nombre de la tarea (dejar vacío para no cambiar): ")
    description = input("Ingrese la nueva descripción de la tarea (dejar vacío para no cambiar): ")
    is_done = input("¿La tarea está completada? (s/n): ").lower() == 's'
    task = update_task(task_id, name, description, is_done)
    if task:
        print(f"Tarea actualizada: {task}")
    else:
        print("Tarea no encontrada.")
    print("===============================")

def delete_task_menu():
    print("=== ELIMINAR TAREA ===")
    task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
    task = delete_task(task_id)
    if task:
        print(f"Tarea eliminada: {task}")
    else:
        print("Tarea no encontrada.")
    print("===============================")