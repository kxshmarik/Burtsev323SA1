import time

# Создаем списка
spisok = list(range(100000))

# Тест удаления из начала списка
start_time = time.time()
for _ in range(1000):
    spisok.pop(0)
time_pop0 = time.time() - start_time

# Восстанавливаем список
spisok = list(range(100000))

# Тест удаления с конца списка
start_time = time.time()
for _ in range(1000):
    spisok.pop()
time_pop = time.time() - start_time

print(f"Время удаления из начала (pop(0)): {time_pop0:.4f} секунд")
print(f"Время удаления с конца (pop()): {time_pop:.4f} секунд")

# Вывод: операция pop() быстрее, чем pop(0)
# - pop() имеет сложность O(1) - удаление с конца не требует перемещения элементов
# - pop(0) имеет сложность O(n) - удаление из начала требует сдвига всех оставшихся элементов