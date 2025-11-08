text = input("Введите произвольную строку: ").lower()
slovar = {}
for a in text:
    if a in slovar:
        slovar[a] += 1
    else:
        slovar[a] = 1
print("Результат подсчёта символов:")
print(slovar)