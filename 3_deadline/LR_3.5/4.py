import time
import random

# Медленное решение (дано)
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# Быстрое решение O(n)
def find_pair_fast(arr, target):
    videno = set()
    for chislo in arr:
        raznica = target - chislo
        if raznica in videno:
            return (chislo, raznica)
        videno.add(chislo)
    return None

# Создаем большой список
bolshoy_spisok = [random.randint(0, 10000) for _ in range(10000)]
tsel = 15000  # Целевая сумма

# Тестируем медленную версию
start_time = time.time()
para_slow = find_pair_slow(bolshoy_spisok, tsel)
time_slow = time.time() - start_time

# Тестируем быструю версию
start_time = time.time()
para_fast = find_pair_fast(bolshoy_spisok, tsel)
time_fast = time.time() - start_time

print("Результаты поиска пары чисел:")
print(f"Медленная версия (O(n^2)): {para_slow}, время: {time_slow:.6f} сек")
print(f"Быстрая версия (O(n)): {para_fast}, время: {time_fast:.6f} сек")
print(f"\nУскорение в {time_slow/time_fast:.1f} раз")