class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    
    def show_tasks(self):
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")
    
    def get_high_priority_tasks(self, min_priority):
        # Возвращаем список задач с приоритетом
        vazhnye_zadachi = []
        for task in self.tasks:
            if task.priority >= min_priority:
                vazhnye_zadachi.append(task)
        return vazhnye_zadachi


# Пример использования
manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.add_task("Не покупать хлеб", 3)
manager.add_task("Не делать домашку", 8)

print("Все задачи:")
manager.show_tasks()

print("\nВажные задачи (с приоритетом 5+):")
important = manager.get_high_priority_tasks(5)
for task in important:
    print(task.description)