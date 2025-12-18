vvod = input("Введите строку: ")
glasn = "аеёыоэяиюaeiouy"
itog = ""
index = 0
while index < len(vvod):
    simvol = vvod[index]
    if simvol.lower() not in glasn:
        itog += simvol
    index += 1
print(f"Результат: {itog}")