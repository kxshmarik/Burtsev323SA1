import random

def repeat():
    def decorator(func):
        def wrapper(*args, **kwargs):
            kolvo = random.randint(1, 10) # n раз = 0-10
            for _ in range(kolvo):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Использование
@repeat()
def privet(name):
    print(f"Привет, {name}!")
@repeat()
def bb(name):
    print(f"Всего доброго, {name}!")

# Будет выполнено случайное количество раз
privet("Вася")
print()
bb("Ашот")