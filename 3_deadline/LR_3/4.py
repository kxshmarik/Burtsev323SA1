def find_max(arr: list) -> int:
    # Пустой список
    if not arr:
        return None
    
    # Список из одного элемента
    if len(arr) == 1:
        return arr[0]
    
    # Разделяем список на две части
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно находим максимумы в каждой половине
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    
    # Комбинирование результатов
    return max_left if max_left > max_right else max_right

# Примеры использования
numbers = [3, 7, 1, 9, 4, 2]
print("Максимум в списке:", find_max(numbers))

print("Максимум в [5]:", find_max([5]))
print("Максимум в [10, 2, 8, 15, 3]:", find_max([10, 2, 8, 15, 3]))
print("Максимум в []:", find_max([]))