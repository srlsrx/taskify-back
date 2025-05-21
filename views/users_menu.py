from controllers.user_controller import (
    get_user_by_id,
    get_all_users,
    create_user,
    update_user,
    delete_user,
)
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_users_menu():
    while True:
        limpiar_consola()
        print("\033[1;96m╔═════════════════════════════╗")
        print("║        MENÚ DE USUARIOS     ║")
        print("╠═════════════════════════════╣")
        print("\033[0m\033[1;93m║ 1. Crear usuario            ║")
        print("║ 2. Ver todos los usuarios   ║")
        print("║ 3. Ver usuario por ID       ║")
        print("║ 4. Actualizar usuario       ║")
        print("║ 5. Eliminar usuario         ║")
        print("║ \033[91m6. Salir   \033[0m\033[1;93m                 ║")
        print("\033[1;96m╚═════════════════════════════╝\033[0m")
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
            print("\033[91mOpción no válida. Intente de nuevo.\033[0m")


def create_user_menu():
    print("=== CREAR USUARIO ===")
    username = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el correo electrónico: ")
    password = input("Ingrese la contraseña: ")
    user = create_user(username, email, password)
    print(f"Usuario creado: Username: {user.username}, Correo: {user.email}, Admin: {user.is_admin}")
    print("=====================")


def get_all_users_menu():
    print("=== TODOS LOS USUARIOS ===")
    users = get_all_users()
    if users:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Correo: {user.email}")
    print("===============================")


def get_user_by_id_menu():
    print("=== CONSULTAR USUARIO POR ID ===")
    user_id = int(input("Ingrese el ID del usuario: "))
    user = get_user_by_id(user_id)
    if user:
        print(f"Usuario encontrado: Username: {user.username}, Correo: {user.email}, Admin: {user.is_admin}")
    print("===============================")


def update_user_menu():
    print("=== ACTUALIZAR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario a actualizar: "))
    username = input("Ingrese el nuevo nombre de usuario (dejar vacío para no cambiar): ")
    email = input("Ingrese el nuevo correo electrónico (dejar vacío para no cambiar): ")
    password = input("Ingrese la nueva contraseña (dejar vacío para no cambiar): ")
    is_admin = input("¿Es administrador? (s/n): ").lower() == "s"
    user = update_user(user_id, username, email, password, is_admin)
    if user:
        print(f"Usuario actualizado: Username: {user.username}, Correo: {user.email}, Admin: {user.is_admin}")
    print("===============================")


def delete_user_menu():
    print("=== ELIMINAR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario a eliminar: "))
    user = delete_user(user_id)
    if user:
        print(f"Usuario eliminado: {user.username}")
    print("===============================")
