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
        print("\033[1;96m╔══════════════════════════════════════╗")
        print("║        ✅  MENÚ TO-DO LIST           ║")
        print("╠══════════════════════════════════════╣")
        print("║ \033[1;93m1.\033[1;96m Crear tarea                       ║")
        print("║ \033[1;93m2.\033[1;96m Ver todas las tareas              ║")
        print("║ \033[1;93m3.\033[1;96m Ver tarea por ID                  ║")
        print("║ \033[1;93m4.\033[1;96m Ver tareas por usuario            ║")
        print("║ \033[1;93m5.\033[1;96m Actualizar tarea                  ║")
        print("║ \033[1;93m6.\033[1;96m Eliminar tarea                    ║")
        print("║ \033[1;91m7.\033[1;96m Salir                             ║")
        print("╚══════════════════════════════════════╝\033[0m")

        choice = input("\033[1mSeleccione una opción: \033[0m")
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
        print("\033[1;96m╔══════════════════════════════════════╗")
        print("║        📋  MENÚ TO-DO LIST           ║")
        print("╠══════════════════════════════════════╣")
        print("║ \033[1;93m1.\033[1;96m Crear tarea                       ║")
        print("║ \033[1;93m2.\033[1;96m Ver mis tareas                    ║")
        print("║ \033[1;93m3.\033[1;96m Actualizar tarea                  ║")
        print("║ \033[1;93m4.\033[1;96m Eliminar tarea                    ║")
        print("║ \033[1;91m5.\033[1;96m Salir                             ║")
        print("╚══════════════════════════════════════╝\033[0m")

        choice = input("\033[1mSelecciona una opción (1-5): \033[0m")
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
    limpiar_consola()
    print("\033[1;96m╔═══════════════════════════════╗")
    print("║        ✏️  CREAR TAREA         ║")
    print("╚═══════════════════════════════╝\033[0m")

    if utils.session.current_user.is_admin:
        print("\033[1m(Eres administrador, puedes asignar tareas a otros usuarios)\033[0m")
        print("")
        name = input("\033[1;93m📌 Nombre de la tarea: \033[0m")
        description = input("\033[1;93m📝 Descripción: \033[0m")
        try:
            id = int(input("\033[1;93m👤 ID del usuario asignado: \033[0m"))
        except ValueError:
            print("\033[1;91mID inválido. Debe ser un número entero.\033[0m")
            return
        task = create_task(name, description, id)
    else:
        name = input("\033[1;93m📌 Nombre de la tarea: \033[0m")
        description = input("\033[1;93m📝 Descripción: \033[0m")
        task = create_task(name, description, utils.session.current_user.id)

    print()
    if task:
        print(f"\033[1;92m✅ Tarea creada:\033[0m {task}")
    else:
        print("\033[1;91m❌ No se pudo crear la tarea.\033[0m")

    input("\n\033[1;90mPulsa ENTER para continuar...\033[0m")


def get_all_tasks_menu():
    limpiar_consola()
    print("\033[1;96m╔══════════════════════════════╗")
    print("║       📋 TODAS LAS TAREAS    ║")
    print("╚══════════════════════════════╝\033[0m")

    tasks = get_all_tasks()

    if tasks:
        for task in tasks:
            print(f"\033[1;93m• {task}\033[0m")
    else:
        print("\033[1;91mNo hay tareas registradas.\033[0m")

    print("\033[1;94m══════════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def get_task_by_id_menu():
    limpiar_consola()
    print("\033[1;96m╔══════════════════════════════════════╗")
    print("║      🔍 CONSULTAR TAREA POR ID       ║")
    print("╚══════════════════════════════════════╝\033[0m")

    try:
        task_id = int(input("\033[1;93m🔢 Ingrese el ID de la tarea: \033[0m"))
    except ValueError:
        print("\033[1;91m❌ ID inválido. Debe ser un número entero.\033[0m")
        input("\n\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    task = get_task_by_id(task_id)

    print()
    if task:
        print(f"\033[1;92m✅ Tarea encontrada:\033[0m {task}")
    else:
        print("\033[1;91m❌ No se encontró ninguna tarea con ese ID.\033[0m")

    print("\033[1;94m══════════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


def get_tasks_by_user_menu():
    limpiar_consola()
    print("\033[1;96m╔════════════════════════════════════════════╗")
    print("║     👤 CONSULTAR TAREAS POR USUARIO        ║")
    print("╚════════════════════════════════════════════╝\033[0m")

    try:
        user_id = int(input("\033[1;93m🔢 Ingrese el ID del usuario: \033[0m"))
    except ValueError:
        print("\033[1;91m❌ ID inválido. Debe ser un número entero.\033[0m")
        input("\n\033[1;90mPulsa ENTER para continuar...\033[0m")
        return

    tasks = get_tasks_by_user(user_id)

    print()
    if tasks:
        print(f"\033[1;92m✅ Se encontraron {len(tasks)} tarea(s):\033[0m")
        for task in tasks:
            print(f"\033[1;93m• {task}\033[0m")
    else:
        print("\033[1;91m❌ No se encontraron tareas para este usuario.\033[0m")

    print("\033[1;94m════════════════════════════════════════════\033[0m")
    input("\033[1;90mPulsa ENTER para continuar...\033[0m")


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
