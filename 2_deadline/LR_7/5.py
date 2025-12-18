def format_report(report_title: str, *data: str, **properties: str) -> None:
    """
    Выводит отформатированный отчет.
    
    Args:
        report_title (str): Название отчета.
        *data (str): Произвольное количество позиционных аргументов с пунктами отчета.
        **properties (str): Произвольное количество именованных аргументов с метаданными.
    
    Returns:
        None: Функция только выводит отчет, не возвращает значения.
    """
    print(f"--- Отчет: {report_title} ---")
    print("Данные:")
    if data:
        for item in data:
            print(f" - {item}")
    else:
        print(" - Нет данных")
    print()
    print("Свойства:")
    if properties:
        for key, value in properties.items():
            print(f" - {key}: {value}")
    else:
        print(" - Нет свойств")
    print("------------------------------")

format_report(
    "Ежедневный отчёт",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)
print()
format_report(
    "Еженедельный отчёт",
    "Продажи выросли на 12%",
    "Новых клиентов: 5",
    author="Бурцев323СА1",
    date="2025-11-09"
)
print()
format_report("Пустой отчёт")