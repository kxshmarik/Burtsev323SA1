vvod = input("Введите 3 целых числа через пробел: ")
c1, c2, c3 = map(int, vvod.split())
u1 = c1 * c2
u2 = c2 * c3
u3 = c3 * c1
stepen = c3 **4
ostatok = c2 % c3
celochisl_d = c3 // c1
summa_punkt5 = stepen + ostatok + celochisl_d
print("Умножение первого на второе:", u1)
print("Умножение второго на третье:", u2)
print("Умножение третьего на первое:", u3)
print("Первое число в 4 степени:", stepen)
print("Остаток от деления второго на третье:", ostatok)
print("Целочисленное деление третьего на первое:", celochisl_d)
print("Сумма результатов из пункта 5:", summa_punkt5)