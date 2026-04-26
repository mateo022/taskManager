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
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        if not description:
            print("Error: La descripción de la tarea no puede estar vacía.")
            return None
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
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
            print(f"Task {id} deleted.")
        else:
            print(f"Task with ID {id} not found.")