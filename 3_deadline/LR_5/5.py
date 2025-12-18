class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority):
        # Создаем новую задачу и добавляем в список
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    
    def show_tasks(self):
        # Выводим все задачи
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")


# Пример использования
manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.show_tasks()