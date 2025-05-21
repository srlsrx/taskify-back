from controllers.user_controller import (
    get_user_by_id,
    get_all_users,
    create_user,
    update_user,
    delete_user,
)


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
    if users:
        for user in users:
            print(f"ID: {user.id}, Nombre: {user.username}, Correo: {user.email}")
    print("===============================")


def get_user_by_id_menu():
    print("=== CONSULTAR USUARIO POR ID ===")
    user_id = int(input("Ingrese el ID del usuario: "))
    user = get_user_by_id(user_id)
    if user:
        print(f"Usuario encontrado: {user}")
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
    print("===============================")


def delete_user_menu():
    print("=== ELIMINAR USUARIO ===")
    user_id = int(input("Ingrese el ID del usuario a eliminar: "))
    user = delete_user(user_id)
    if user:
        print(f"Usuario eliminado: {user}")
    print("===============================")
