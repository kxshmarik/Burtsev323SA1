simvol = input("Символ: ")
visota = int(input("Высота: "))
shirina = int(input("Ширина: "))
if visota <= 0 or shirina <= 0:
    print("Ошибка: высота и ширина должны быть больше 0")
else:
    i = 0
    while i < visota:
        j = 0
        stroka = ""
        while j < shirina:
            stroka += simvol
            j += 1
        print(stroka)
        i += 1