import time

def timer(func):
    def wrapper(*args, **kwargs):
        nachalo = time.time()
        result = func(*args, **kwargs)
        konec = time.time()
        vremya = konec - nachalo
        print(f"Время выполнения функции {func.__name__}: {vremya:.4f} сек")
        return result
    return wrapper

@timer
def slow_func():
    for _ in range(1000000):
        pass
     
@timer
def sum_numbers(n):
    # Суммирует числа от 1 до n
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Примеры использования
slow_func()
sum_numbers(1000000)
