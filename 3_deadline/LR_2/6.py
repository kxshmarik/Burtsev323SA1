def flat_gen(nested_list: list):
    for sublist in nested_list:
        yield from sublist
        
# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

print("Выпрямленная матрица:")
for num in flat_gen(matrix):
    print(num, end=" ")