my_gen = (num for num in range(10, 21) if num % 2 == 0)
print("Четные числа от 10 до 20:")
for num in my_gen:
    print(num)