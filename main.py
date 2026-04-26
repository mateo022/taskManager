from task_manager import TaskManager

def print_menu():
        print("-------------Gestor de tareas Inteligente------------------")
        print("Comandos disponibles: add, list, complete, delete, exit")
        print("1. add <descripción>: Agrega una nueva tarea")
        print("2. list: Lista todas las tareas")
        print("3. complete <id>: Marca una tarea como completada")
        print("4. delete <id>: Elimina una tarea")
        print("5. exit: Salir del programa")


def main():
    task_manager = TaskManager()

    while True:

        print_menu()
        choice = input("Ingrese un comando: ")

        match choice:
            case "1":
                description = input("Ingrese la descripción de la tarea: ")
                task = task_manager.add_task(description)
                print(f"Tarea agregada: {task}")
            case "2":
                tasks = task_manager.list_tasks()
                for task in tasks:
                    print(task)
            case "3":
                id = int(input("Ingrese el ID de la tarea a completar: "))
                task_manager.complete_task(id)
            case "4":
                id = int(input("Ingrese el ID de la tarea a eliminar: "))
                task_manager.delete_task(id)
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Comando no reconocido. Por favor, intente de nuevo.")    
if __name__ == "__main__":    
        main()    