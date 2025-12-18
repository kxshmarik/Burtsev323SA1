def squares_gen(n: int):
    for i in range(1, n + 1):
        yield i * i

# Пример использования
gen = squares_gen(12)
for val in gen:
    print(val)