text = input("Введите произвольный текст: ")
shag = int(input("Введите шаг: "))
swaga = text[::shag]
print("Текст с шагом", shag,"->",swaga)