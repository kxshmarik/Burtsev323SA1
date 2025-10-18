import math
print("Список возможных операций: умножение(*), деление(/), сложение(+), вычитание(-), остаток от деления(%), деление без остатка(//), возведение в степень(**), процентов от числа(%%), корень(**)")
virazhenie = input("Введите выражение в формате 'число1 знак число2': ")
c1, znak, c2 = virazhenie.split()
chislo1 = float(c1)
chislo2 = float(c2)
resultat = None
if znak == '+':
    resultat = chislo1 + chislo2
elif znak == '-':
    resultat = chislo1 - chislo2
elif znak == '*':
    resultat = chislo1 * chislo2
elif znak == '/':
    if chislo2 != 0:
        resultat = chislo1 / chislo2
    else:
        print("Ошибка: деление на ноль!")
elif znak == '%':
    resultat = chislo1 % chislo2
elif znak == '//':
    if chislo2 != 0:
        resultat = chislo1 // chislo2
    else:
        print("Ошибка: деление на ноль!")
elif znak == '**':
    resultat = chislo1 ** chislo2
elif znak == '%%':
    resultat = chislo2 * 100 / chislo1
elif znak == '/**':
    if chislo1 >= 0:
        resultat = math.sqrt(chislo1)
    else:
        print("Ошибка: нельзя извлечь корень из отрицательного числа!")
else:
    print("Неккоректный ввод!")
if resultat is not None:
    print(f"Результат: {resultat}")