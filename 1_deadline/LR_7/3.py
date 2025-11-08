text = input("Введите произвольный текст: ")
slovo = input("Введите слово для поиска: ")
if slovo in text:
    kolvo = text.count(slovo)
    print(f"Слово '{slovo}' найдено в тексте")
    print(f"Количество совпадений: {kolvo}")
else:
    print(f"Слово '{slovo}' не найдено в тексте")