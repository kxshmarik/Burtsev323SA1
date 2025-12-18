class Multiplier:
    def __init__(self, multiplier):
        # При инициализации запоминает число-множитель
        self.multiplier = multiplier
    
    def __call__(self, number):
        # Вызываем объект как функцию
        return number * self.multiplier


# Пример использования
by_5 = Multiplier(5)
print(by_5(10))   # 50
print(by_5(2))    # 10
print(by_5(-3))   # -15