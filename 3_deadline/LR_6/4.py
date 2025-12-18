import time

class Timer:
    def __enter__(self):
        # Запоминаем время начала
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Вычисляем время выполнения
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        
        # Выводим время выполнения
        print(f"Время выполнения: {elapsed_time:.2f} сек")
        
        # Если была ошибка то передаем её дальше
        return False


# Пример использования
print("Замер времени для sleep(1.5):")
with Timer():
    time.sleep(1.5)

print("\nЗамер времени для цикла:")
with Timer():
    sum(range(1000000))

# Пример с ошибкой
print("\nПример с ошибкой (деление на ноль):")
try:
    with Timer():
        result = 10 / 0
except ZeroDivisionError:
    print("Произошла ошибка деления на ноль!")