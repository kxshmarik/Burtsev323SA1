import sys

def create_list(n):
    # Создает обычный список
    spisok = []
    for i in range(n):
        spisok.append(i ** 2)
    return spisok

def create_gen(n):
    # Создает генератор
    return (i ** 2 for i in range(n))

n = 1000000

# Создаем оба объекта
spisok = create_list(n)
generator = create_gen(n)

# Сравниваем размер в памяти
print(f"Размер списка из {n} элементов: {sys.getsizeof(spisok)} байт")
print(f"Размер генератора: {sys.getsizeof(generator)} байт")

# - Список имеет сложность O(n) по памяти, так как хранит все элементы
# - Генератор имеет сложность O(1) по памяти, так как генерирует элементы по одному