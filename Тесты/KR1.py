data = input("Введите дату для проверки корректности в формате 'дд.мм.гггг': ")
if len(data) != 10 or data[2] != '.' or data[5] != '.':
    print("Ошибка")
else:
    parts = data.split('.')
    if len(parts) != 3 or not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        print("Ошибка")
    else:
        den = int(parts[0])
        mesyac = int(parts[1])
        god = int(parts[2])
        if god < 1900 or god > 2025:
            print("Ошибка")
        elif mesyac < 1 or mesyac > 12:
            print("Ошибка")
        elif mesyac in [1, 3, 5, 7, 8, 10, 12]:
            if den < 1 or den > 31:
                print("Ошибка")
            else:
                print("Корректно")
        elif mesyac in [4, 6, 9, 11]:
            if den < 1 or den > 30:
                print("Ошибка")
            else:
                print("Корректно")
        elif mesyac == 2:
            if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0):
                if den < 1 or den > 29:
                    print("Ошибка")
                else:
                    print("Корректно")
            else:
                if den < 1 or den > 28:
                    print("Ошибка")
                else:
                    print("Корректно")