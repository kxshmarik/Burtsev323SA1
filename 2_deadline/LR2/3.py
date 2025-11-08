text = input("Введите текст: ")
bukv = 0
cifr = 0
znakipp = 0
probel = 0
znak = ".,!?:;"
lat = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
rus = "йцукенгшщзхъфывапролджэячсмиптьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
cifra = "0123456789"
for simvol in text:
    if simvol in lat or simvol in rus:
        bukv += 1
    elif simvol in cifra:
        cifr += 1
    elif simvol in znak:
        znakipp += 1
    elif simvol == ' ':
        probel += 1
print(f"Букв = {bukv}")
print(f"Цифр = {cifr}")
print(f"Знаков препинания = {znakipp}")
print(f"Пробелов = {probel}")