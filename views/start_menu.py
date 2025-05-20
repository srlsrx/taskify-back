from controllers.task_controller import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    get_tasks_by_user,
)

from controllers.user_controller import (
    get_user_by_id,
    get_all_users,
    create_user,
    update_user,
    delete_user,
)

from models.task_model import Task
from models.user_model import User


# =================== MENÚ INICIAL ===================
def display_start_menu():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Usuarios")
        print("2. Tareas")
        print("3. Salir")
        print("=========================")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            display_users_menu()
        elif choice == "2":
            display_tasks_menu()
        elif choice == "3":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# =================== MENÚ USUARIOS ===================
def display_users_menu():
    while True:
        print("=== MENÚ USUARIOS ===")
        print("1. Crear usuario")
        print("2. Ver todos los usuarios")
        print("3. Ver usuario por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Salir")
        print("=========================")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            create_user_menu()
        elif choice == "2":
            get_all_users_menu()
        elif choice == "3":
            get_user_by_id_menu()
        elif choice == "4":
            update_user_menu()
        elif choice == "5":
            delete_user_menu()
        elif choice == "6":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def create_user_menu():
    print("=== CREAR USUARIO ===")
    username = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el correo electrónico: ")
    password = input("Ingrese la contraseña: ")
    user = create_user(username, email, password)
    print(f"Usuario creado: {user}")
    print("=====================")


def get_all_users_menu():
    print("=== TODOS LOS USUARIOS ===")
    users = get_all_users()
    for user in users:
        print(user)
    print("===============================")


def get_user_by_id_menu():
    print("=== CONSULTAR USUARIO POR ID ===")
    user_id = int(input("Ingrese el ID del usuario: "))
    user = get_user_by_id(user_id)
    if user:
        print(f"Usuario encontrado: {user}")
    else:
        print("Usuario no encontrado.")
    print("===============================")


def update_user_menu():
    print("=== ACTUALIZAR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario a actualizar: "))
    username = input("Ingrese el nuevo nombre de usuario (dejar vacío para no cambiar): ")
    email = input("Ingrese el nuevo correo electrónico (dejar vacío para no cambiar): ")
    password = input("Ingrese la nueva contraseña (dejar vacío para no cambiar): ")
    user = update_user(user_id, username, email, password)
    if user:
        print(f"Usuario actualizado: {user}")
    else:
        print("Usuario no encontrado.")
    print("===============================")


def delete_user_menu():
    print("=== ELIMINAR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario a eliminar: "))
    user = delete_user(user_id)
    if user:
        print(f"Usuario eliminado: {user}")
    else:
        print("Usuario no encontrado.")
    print("===============================")


# =================== MENÚ TAREAS ===================
def display_tasks_menu():
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
    description = input(
        "Ingrese la nueva descripción de la tarea (dejar vacío para no cambiar): "
    )
    is_done = input("¿La tarea está completada? (s/n): ").lower() == "s"
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
