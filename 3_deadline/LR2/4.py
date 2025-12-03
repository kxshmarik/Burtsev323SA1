def my_range(start: float, end: float, step: float = 1.0):
    current = start
    while current < end:
        yield current
        current += step
print("Числа от 1 до 10 с шагом 0.5:")
for i in my_range(1, 10, 0.5):
    print(i)