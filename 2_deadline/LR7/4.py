call_counter = 0
def increment_counter() -> None:
    """
    Увеличивает call_counter на 1 при каждом вызове.
    
    Returns:
        None: Функция не возвращает значения
    """
    global call_counter
    call_counter += 1
print(f"Начальное значение: {call_counter}")
increment_counter()
increment_counter()
increment_counter()
print(f"После трех вызовов: {call_counter}")
increment_counter()
increment_counter()
print(f"После пяти вызовов: {call_counter}")