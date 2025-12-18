def binary_search(arr: list, target: int, left: int = 0, right: int = None) -> int:
    # Инициализируем правую границу при первом вызове
    if right is None:
        right = len(arr) - 1
    
    # Границы пересеклись, элемент не найден
    if left > right:
        return -1
    
    # Находим середину
    mid = (left + right) // 2
    
    # Элемент найден
    if arr[mid] == target:
        return mid
    
    # Ищем в левой половине, если target меньше середины
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    # Ищем в правой половине, если target больше середины
    else:
        return binary_search(arr, target, mid + 1, right)

# Примеры использования
my_list = [10, 20, 30, 40, 50, 60, 70]

print("Поиск 40:", binary_search(my_list, 40))
print("Поиск 10:", binary_search(my_list, 10))
print("Поиск 70:", binary_search(my_list, 70))
print("Поиск 99:", binary_search(my_list, 99))
print("Поиск 25:", binary_search(my_list, 25))