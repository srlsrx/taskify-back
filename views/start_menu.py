

from models.task_model import Task
from models.user_model import User
from views.users_menu import display_users_menu
from views.tasks_menu import display_tasks_menu
from controllers.user_controller import get_user_by_username
from utils.session import current_user

# =================== MENÚ INICIAL ===================
def display_login_menu():
    print("=== MENÚ DE INICIO DE SESIÓN ===")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if not username or not password:
        print("El nombre de usuario y la contraseña son obligatorios.")
        return None
    user = get_user_by_username(username)
    if username == user.username and password == user.password:
        current_user.user_id = user.id
        if user.is_admin:
            display_admin_menu()
        else:
            display_tasks_menu()
    else:
        print("Nombre de usuario o contraseña incorrectos.")
    print("===============================")

def display_admin_menu():
    while True:
        print("=== MENÚ ADMINISTRADOR ===")
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


display_login_menu()
