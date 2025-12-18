def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    # Складывает a + b
    return a + b

@logger
def multiply(a, b, c=1):
    # Умножает три числа (третье по умолчанию 1)
    return a * b * c

# Примеры использования
add(5, 10)
multiply(2, 3)
multiply(2, 3, c=4)