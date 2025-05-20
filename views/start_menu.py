

from models.task_model import Task
from models.user_model import User
from views.users_menu import display_users_menu
from views.tasks_menu import display_tasks_menu

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


display_start_menu()
