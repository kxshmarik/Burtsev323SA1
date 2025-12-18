def calc_avg(numbers: list[float]) -> float:
    """
    Вычисляет среднее арифметическое значение списка чисел.
    
    Args:
        numbers (list[float]): Список чисел для вычисления среднего.
    
    Returns:
        float: Среднее арифметическое значение.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    """
    Форматирует ФИО из списка частей.
    
    Args:
        parts (list[str]): Список частей ФИО.
        capitalize (bool, optional): Приводить ли первую букву каждого слова к верхнему регистру. 
    
    Returns:
        str: Отформатированное ФИО.
    """
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio

def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    """
    Фильтрует словарь оценок, оставляя только те, которые не ниже минимального значения.
    
    Args:
        data_dict (dict[str, int]): Словарь с названиями предметов и оценками.
        min_value (int): Минимальное значение оценки для включения в результат.
    
    Returns:
        dict[str, int]: Отфильтрованный словарь с оценками не ниже необходимых (min_value).
    """
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value   
    return result

print(calc_avg([10, 20, 30, 40]))
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
scores = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(scores, 90))