import random
import string

vvod = input("Введите сообщение: ")
n = int(input("Введите число подстановочных символов: "))
def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
secret = ""
for bukva in vvod:
    randomsimv = generate_random_string(n)
    secret += bukva + randomsimv
print("Закодированное сообщение: ", secret) 