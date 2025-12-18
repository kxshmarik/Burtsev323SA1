summa = 0
while True:
    chislo = int(input("Введите числа (для завершения введите 0): "))
    if chislo == 0:
        break
    summa += 1
print(f"Количество введёных чисел: {summa}")