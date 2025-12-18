class SmartList(list):
    def __getitem__(self, index):
        # Изменяем поведение
        if isinstance(index, int) and index < 0:
            # Для отрицательных индексов: -1 -> 0, -2 -> 1 и т.д.
            return super().__getitem__(-index - 1)
        else:
            # Для положительных индексов и срезов работает как обычно
            return super().__getitem__(index)


# Пример использования
sl = SmartList([10, 20, 30, 40, 50])

print("Элементы списка:", sl)
print(sl[0])     # 10
print(sl[1])     # 20
print(sl[-1])    # 10 (в обычном списке было бы 50)
print(sl[-2])    # 20 (в обычном списке было бы 40)
print(sl[-3])    # 30 (в обычном списке было бы 30)