tasks = []
while True:
    print("--- Меню задач ---")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    choice = input("Выбрано действие: ")
    if choice == '1':
        if not tasks:
            print("Список задач пуст!")
        else:
            print("Ваши задачи:")
            for a, task in enumerate(tasks, 1):
                print(f"{a}. {task}")
    elif choice == '2':
        new_task = input("Введите описание задачи: ")
        tasks.append(new_task)
        print(f"Задача '{new_task}' добавлена!")
    elif choice == '3':
        if not tasks:
            print("Список задач пуст!")
        else:
            print("Ваши задачи:")
            for a, task in enumerate(tasks, 1):
                print(f"{a}. {task}")
            try:
                task_num = int(input("Какую задачу выполнили? "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Задача '{removed_task}' удалена!")
                else:
                    print("Неверный номер задачи!")
            except ValueError:
                print("Введите корректный номер!")
    elif choice == '4':
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор!")