import time

# Функция бинарного поиска
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    sredina = (left + right) // 2
    
    if arr[sredina] == target:
        return sredina
    elif arr[sredina] > target:
        return binary_search(arr, target, left, sredina - 1)
    else:
        return binary_search(arr, target, sredina + 1, right)

# Функция линейного поиска
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Создаем большой отсортированный список
bolshoy_spisok = list(range(10000000))
iskomoe = -1

# Тестируем бинарный поиск
start_time = time.time()
rezultat_bin = binary_search(bolshoy_spisok, iskomoe)
time_bin = time.time() - start_time

# Тестируем линейный поиск
start_time = time.time()
rezultat_lin = linear_search(bolshoy_spisok, iskomoe)
time_lin = time.time() - start_time

# Вывод
print(f"Бинарный поиск (O(log n)): результат {rezultat_bin}, время {time_bin:.6f} сек")
print(f"Линейный поиск (O(n)): результат {rezultat_lin}, время {time_lin:.6f} сек")

if time_lin > time_bin:
    print(f"\nБинарный поиск быстрее в {time_lin/time_bin:.0f} раз")
else:
    print("\nАшот неожиданно ускорил линейный поиск и он оказался быстрее (такого не должно быть)")