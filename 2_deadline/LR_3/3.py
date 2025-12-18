phone_book = {
    'Ашот Похититель': '+79123456789',
    'Виктор Губачёс': '+79234567890',
    'Произвольная запись': '+79345678901'
}
while True:
    print("Телефонная книга")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    vibor = input("Выберите действие: ")
    if vibor == '1':
        print("Ваши контакты:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    elif vibor == '2':
        name = input("Введите имя: ")
        if name in phone_book:
            print("Контакт с таким именем уже существует!")
        else:
            phone = input("Введите номер телефона: ")
            phone_book[name] = phone
            print(f"Контакт {name} добавлен!")
    elif vibor == '3':
        name = input("Введите имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт {name} удален!")
        else:
            print("Контакт с таким именем не найден!")
    elif vibor == '4':
        print("Выход из программы...")
        exit()
    else:
        print("Неверный выбор! Попробуйте снова.")