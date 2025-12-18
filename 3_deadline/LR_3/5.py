import time

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tail_fibonacci(n: int, a: int = 0, b: int = 1) -> int:
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)

# Сравнение производительности
n = 35

print("=== Сравнение производительности рекурсий ===")

# Замер обычной рекурсии
start_time = time.time()
result1 = fibonacci(n)
time1 = time.time() - start_time
print(f"Fibonacci({n}) = {result1}")
print(f"Время обычной рекурсии: {time1:.6f} секунд")

# Замер хвостовой рекурсии
start_time = time.time()
result2 = tail_fibonacci(n)
time2 = time.time() - start_time
print(f"\nTail Fibonacci({n}) = {result2}")
print(f"Время хвостовой рекурсии: {time2:.6f} секунд")

# Сравнение результатов
if result1 == result2:
    print(f"\nРезультаты совпадают: {result1}")
else:
    print(f"\nРезультаты не совпадают: {result1} != {result2}")

print(f"\nХвостовая рекурсия быстрее в {time1/time2:.1f} раз")