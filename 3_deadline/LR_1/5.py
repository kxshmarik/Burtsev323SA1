def safe_exec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
            return 0
    return wrapper

@safe_exec
def divide(a, b):
    # Делит a на b
    return a / b

@safe_exec
def calculate(x, y, z):
    # Выполняет вычисление: (x + y) / z
    return (x + y) / z

# Примеры использования
print(f"Результат 1: {divide(10, 2)}")
print(f"Результат 2: {divide(5, 0)}")
print(f"Результат 3: {calculate(10, 20, 5)}")
print(f"Результат 4: {calculate(10, 20, 0)}")