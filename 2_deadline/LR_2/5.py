kolvo = int(input("Сколько чисел вы хотите ввести? "))
chisla = []
for a in range(kolvo):
    chislo = float(input(f"Введите число {a + 1}: "))
    chisla.append(chislo)
max_chislo = max(chisla)
min_chislo = min(chisla)
srednee = sum(chisla) / len(chisla)
schet = 0
for chislo in chisla:
    if chislo > srednee:
        schet += 1
print("Результаты:")
print(f"Максимальное = {max_chislo}")
print(f"Минимальное = {min_chislo}")
print(f"Среднее = {srednee}")
print(f"Чисел больше среднего = {schet}")