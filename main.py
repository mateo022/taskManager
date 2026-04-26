from task_manager import TaskManager

def print_menu():
        print("------------- Gestor de tareas Inteligente ------------------")
        print("1. Agrega una nueva tarea")
        print("2. Lista todas las tareas")
        print("3. Marca una tarea como completada")
        print("4. Elimina una tarea")
        print("5. Salir del programa")


def main():
    task_manager = TaskManager()

    while True:

        print_menu()

        try:
             
            choice = int(input("Ingrese un opción: "))


            match choice:
                case 1:
                    description = input("Ingrese la descripción de la tarea: ")
                    task = task_manager.add_task(description)
                    print(f"Tarea agregada: {task}")
                case 2:
                    tasks = task_manager.list_tasks()
                    for task in tasks:
                        print(task)
                case 3:
                    id = int(input("Ingrese el ID de la tarea a completar: "))
                    task_manager.complete_task(id)
                case 4:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    task_manager.delete_task(id)
                case 5:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no reconocida. Por favor, intente de nuevo.")    
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número correspondiente a las opciones.")
if __name__ == "__main__":    
        main()    