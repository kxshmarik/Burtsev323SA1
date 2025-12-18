# Создание генераторного выражения для четных чисел от 10 до 20
my_gen = (num for num in range(10, 21) if num % 2 == 0)

# Вывод чисел
print("Четные числа от 10 до 20:")
for num in my_gen:
    print(num)