stroka = input("Введите строку: ")
ignor = stroka.replace(" ", "").lower()
lr = 0
rl = len(ignor) - 1
palin = True
while lr < rl:
    if ignor[lr] != ignor[rl]:
        palin = False
        break
    lr += 1
    rl -= 1
if palin:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")