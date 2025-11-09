def find_common_elements(list1: list, list2: list) -> list:
    """
    Находит общие элементы между двумя списками без дубликатов.
    
    Args:
        list1 (list): Первый список для сравнения.
        list2 (list): Второй список для сравнения.
    
    Returns:
        list: Список элементов без дубликатов.
    """
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list1, list2)
print(f"Общие элементы: {common}")