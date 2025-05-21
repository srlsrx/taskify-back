from controllers.user_controller import (
    get_user_by_id,
    get_all_users,
    create_user,
    update_user,
    delete_user,
)
import os


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


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
    limpiar_consola()
    print("\033[1;96m╔════════════════════════════════╗")
    print("║         ➕ CREAR USUARIO        ║")
    print("╚════════════════════════════════╝\033[0m")

    username = input("\033[1;93m👤 Nombre de usuario: \033[0m")
    email = input("\033[1;93m📧 Correo electrónico: \033[0m")
    password = input("\033[1;93m🔒 Contraseña: \033[0m")

    user = create_user(username, email, password)

    print()
    if user:
        print("\033[1;92m✅ Usuario creado correctamente:\033[0m")
        print(f"\033[1;96m• Nombre de usuario:\033[0m {user.username}")
        print(f"\033[1;96m• Correo electrónico:\033[0m {user.email}")
        print(f"\033[1;96m• ¿Es admin?:\033[0m {'Sí' if user.is_admin else 'No'}")
    else:
        print("\033[1;91m❌ No se pudo crear el usuario.\033[0m")

    print("\033[1;94m════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def get_all_users_menu():
    limpiar_consola()
    print("\033[1;96m╔═════════════════════════════════╗")
    print("║       👥 TODOS LOS USUARIOS      ║")
    print("╚═════════════════════════════════╝\033[0m")

    users = get_all_users()

    if users:
        print("\033[1;93mListado de usuarios:\033[0m\n")
        for user in users:
            print(
                f"\033[1;96m• ID:\033[0m {user.id} \033[1;96m| Usuario:\033[0m {user.username} \033[1;96m|\
                Correo:\033[0m {user.email}"
            )
    else:
        print("\033[1;91m❌ No hay usuarios registrados.\033[0m")

    print("\n\033[1;94m═════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def get_user_by_id_menu():
    limpiar_consola()
    print("\033[1;96m╔══════════════════════════════════════╗")
    print("║     🔍 CONSULTAR USUARIO POR ID      ║")
    print("╚══════════════════════════════════════╝\033[0m")

    try:
        user_id = int(input("\033[1;93m🔢 Ingrese el ID del usuario: \033[0m"))
    except ValueError:
        print("\033[1;91m❌ ID inválido. Debe ser un número entero.\033[0m")
        input("\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    user = get_user_by_id(user_id)

    print()
    if user:
        print("\033[1;92m✅ Usuario encontrado:\033[0m")
        print(f"\033[1;96m• Nombre de usuario:\033[0m {user.username}")
        print(f"\033[1;96m• Correo electrónico:\033[0m {user.email}")
        print(f"\033[1;96m• ¿Es admin?:\033[0m {'Sí' if user.is_admin else 'No'}")
    else:
        print("\033[1;91m❌ No se encontró ningún usuario con ese ID.\033[0m")

    print("\n\033[1;94m══════════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def update_user_menu():
    limpiar_consola()
    print("\033[1;96m╔══════════════════════════════════╗")
    print("║       🔄 ACTUALIZAR USUARIO       ║")
    print("╚══════════════════════════════════╝\033[0m")

    try:
        user_id = int(
            input("\033[1;93m🔢 Ingrese el ID del usuario a actualizar: \033[0m")
        )
    except ValueError:
        print("\033[1;91m❌ ID inválido. Debe ser un número entero.\033[0m")
        input("\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    username = input(
        "\033[1;93m👤 Nuevo nombre de usuario (dejar vacío para no cambiar): \033[0m"
    )
    email = input(
        "\033[1;93m📧 Nuevo correo electrónico (dejar vacío para no cambiar): \033[0m"
    )
    password = input(
        "\033[1;93m🔒 Nueva contraseña (dejar vacío para no cambiar): \033[0m"
    )
    admin_input = input("\033[1;93m👑 ¿Es administrador? (s/n): \033[0m").lower()

    if admin_input == "s":
        is_admin = True
    elif admin_input == "n":
        is_admin = False
    else:
        print("\033[1;91m❌ Opción inválida. El usuario no se actualizará.\033[0m")
        input("\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    user = update_user(user_id, username, email, password, is_admin)

    print()
    if user:
        print("\033[1;92m✅ Usuario actualizado correctamente:\033[0m")
        print(f"\033[1;96m• Usuario:\033[0m {user.username}")
        print(f"\033[1;96m• Correo:\033[0m {user.email}")
        print(f"\033[1;96m• ¿Es admin?:\033[0m {'Sí' if user.is_admin else 'No'}")
    else:
        print("\033[1;91m❌ No se encontró ningún usuario con ese ID.\033[0m")

    print("\033[1;94m══════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def delete_user_menu():
    limpiar_consola()
    print("\033[1;96m╔════════════════════════════════╗")
    print("║        🗑️  ELIMINAR USUARIO       ║")
    print("╚════════════════════════════════╝\033[0m")

    try:
        user_id = int(input("\033[1;93m🔢 Ingrese el ID del usuario a eliminar: \033[0m"))
    except ValueError:
        print("\033[1;91m❌ ID inválido. Debe ser un número entero.\033[0m")
        input("\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    confirm = input("\033[1;93m⚠️ ¿Estás seguro que deseas eliminar este usuario? (s/n): \033[0m").lower()
    if confirm != "s":
        print("\033[1;94mCancelado. El usuario no fue eliminado.\033[0m")
        input("\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    user = delete_user(user_id)

    print()
    if user:
        print(f"\033[1;92m✅ Usuario eliminado:\033[0m {user.username}")
    else:
        print("\033[1;91m❌ No se encontró ningún usuario con ese ID.\033[0m")

    print("\033[1;94m════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")
