def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    
# Пример использования
print("Первые 9 чисел Фибоначчи:")
for num in fibonacci(9):
    print(num)