import random
numbers = [random.randint(1, 100) for a in range(10)]
chet = [num for num in numbers if num % 2 == 0]
b50 = [num for num in numbers if num > 50]
print(f"Исходный список: {numbers}")
print(f"Четные числа: {chet}")
print(f"Числа больше 50: {b50}")