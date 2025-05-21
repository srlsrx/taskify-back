

from models.task_model import Task
from models.user_model import User
from views.users_menu import display_users_menu
from views.tasks_menu import display_users_tasks_menu
from views.tasks_menu import display_admin_tasks_menu
from controllers.user_controller import get_user_by_username
import utils.session
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# =================== MENÚ INICIAL ===================
def display_login_menu():
    limpiar_consola()
    print("\033[1;96m")
    print(" _____         _    _  __      ")
    print("|_   _|_ _ ___| | _(_)/ _|_   _")
    print("  | |/ _` / __| |/ / | |_| | | |")
    print("  | | (_| \\__ \\   <| |  _| |_| |")
    print("  |_|\\__,_|___/_|\\_\\_|_|  \\__, |")
    print("                          |___/ ")
    print("")
    print("      \033[1;95mTo-Do by Julia & Nico\033[1;96m")
    print("════════════════════════════════════\033[0m")

    username = input("\033[1;93m👤 Usuario: \033[0m")
    password = input("\033[1;93m🔒 Contraseña: \033[0m")
    if not username or not password:
        print("\033[91mEl nombre de usuario y la contraseña son obligatorios.\033[0m")
        return None
    user = get_user_by_username(username)
    if user:
        if password == user.password:
            utils.session.current_user = user
            if user.is_admin:
                display_admin_menu()
            else:
                display_users_tasks_menu()
        else:
            print("\033[91mContraseña incorrecta\033[0m")
    print("===============================")

def display_admin_menu():
    while True:
        limpiar_consola()
        print("\033[1;96m╔═══════════════════════════════════════╗")
        print("║         🛠️  MENÚ ADMINISTRADOR         ║")
        print("╠═══════════════════════════════════════╣")
        print("║ \033[1;93m1.\033[1;96m Usuarios                           ║")
        print("║ \033[1;93m2.\033[1;96m Tareas                             ║")
        print("║ \033[1;91m3.\033[1;96m Salir                              ║")
        print("╚═══════════════════════════════════════╝\033[0m")

        choice = input("\033[1mSeleccione una opción: \033[0m")
        if choice == "1":
            display_users_menu()
        elif choice == "2":
            display_admin_tasks_menu()
        elif choice == "3":
            print("Saliendo del menú...")
            break
        else:
            print("\033[91mOpción no válida. Intente de nuevo.\033[0m")


display_login_menu()
