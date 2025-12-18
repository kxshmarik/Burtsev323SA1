vvod = int(input("Введите слитно 3 положительных числа: "))
summa = 0
okak = vvod
while okak > 0:
    vvod = okak % 10
    summa += vvod
    okak = okak // 10
print(f"Сумма цифр: {summa}")