from random import randint
chislo = randint(1, 100)
print("Загадано число от 1 до 100. Попробуй угадать!")
while True:
    trai = int(input("Введите ваше число: "))
    if trai == chislo:
        print(f"Угадал! Ответ: {chislo}")
        break
    elif trai > chislo:
        print("Меньше")
    else:
        print("Больше")