reg1 = input("Введите пароль для регистрации: ")
reg2 = input("Подтвердите пароль: ")
if reg1 == reg2:
    print("Пароль успешно установлен!")
    auth = input("Введите пароль для авторизации: ")
    if auth == reg1:
        print("Access")
    else:
        print("Denied")
else:
    print("Пароли не совпадают!")