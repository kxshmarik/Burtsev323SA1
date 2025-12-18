import time
import random

def find_duplicates(arr):
    # Медленное решение с вложенными циклами O(n^2)
    duplikati = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplikati.append(arr[i])
    return duplikati

# Генерация списка случайных чисел
spisok_5000 = [random.randint(0, 1000) for _ in range(5000)]

# Замер времени для 5000 элементов
start_time = time.time()
rezultat = find_duplicates(spisok_5000)
time_5000 = time.time() - start_time

# Генерация списка в 2 раза больше
spisok_10000 = [random.randint(0, 1000) for _ in range(10000)]

# Замер времени для 10000 элементов
start_time = time.time()
rezultat = find_duplicates(spisok_10000)
time_10000 = time.time() - start_time

print(f"Время выполнения для 5000 элементов: {time_5000:.4f} секунд")
print(f"Время выполнения для 10000 элементов: {time_10000:.4f} секунд")
print(f"Увеличение времени в {time_10000/time_5000:.1f} раз")

# Вопрос: Если данные выросли в 2 раза, во сколько раз выросло время выполнения?
print("\nОтвет: Для алгоритма O(n^2) при увеличении данных в 2 раза время должно вырасти примерно в 4 раза.")
print(f"На деле получилось: {time_10000/time_5000:.1f} раза")