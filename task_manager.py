import json

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.id}: {self.description} [{status}]"
    
class TaskManager:
    
    FILENAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, description):
        if not description:
            print("Error: La descripción de la tarea no puede estar vacía.")
            return None
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task

    def get_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def complete_task(self, id):
        task = self.get_task(id)
        if task:
            task.mark_completed()
            self.save_tasks()
            print(f"Task {id} marked as completed.")
        else:
            print(f"Task with ID {id} not found.")
    def list_tasks(self):
        if not self.tasks:
            return ["No tasks available."]
        return [str(task) for task in self.tasks]
    
    def delete_task(self, id):
        task = self.get_task(id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {id} deleted.")
        else:
            print(f"Task with ID {id} not found.")

    def load_tasks(self):
        try:
            with open(self.FILENAME, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(item['id'], item['description'], item['completed']) for item in data]
                if self.tasks:
                    self.next_id = self.tasks[-1].id + 1
                else:
                    self.next_id = 1 
        except FileNotFoundError:
            print(f"File {self.FILENAME} not found. Starting with an empty task list.")

    def save_tasks(self):
        with open(self.FILENAME, 'w') as file:
            json.dump([
                {
                    "id": task.id,
                    "description": task.description,
                    "completed": task.completed
                }
                for task in self.tasks
            ], file, indent=4)