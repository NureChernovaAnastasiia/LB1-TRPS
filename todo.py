class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task or not task.strip():
            raise ValueError("Task cannot be empty")
        self.tasks.append({"task": task.strip(), "completed": False})
        return len(self.tasks) - 1

    def remove_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        return self.tasks.pop(index)

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        self.tasks[index]["completed"] = True
        return self.tasks[index]

    def uncomplete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        self.tasks[index]["completed"] = False
        return self.tasks[index]

    def get_all_tasks(self):
        return self.tasks.copy()

    def get_completed_tasks(self):
        return [task for task in self.tasks if task["completed"]]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]

    def clear_completed(self):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task["completed"]]
        return initial_count - len(self.tasks)

    def task_count(self):
        return len(self.tasks)

    def completed_count(self):
        return len(self.get_completed_tasks())

    def pending_count(self):
        return len(self.get_pending_tasks())
