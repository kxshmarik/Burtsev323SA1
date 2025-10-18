text = input("Введите произвольный текст: ")
diapazon = input("Введите диапазон в формате 'число1 число2': ")
nachalo, konec = map(int, diapazon.split())
nachalo_index = nachalo - 1
konec_index = konec
podstroka = text[nachalo_index:konec_index]
print("Подстрока по заданному диапазону:",podstroka)