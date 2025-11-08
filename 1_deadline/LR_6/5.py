text = input("Введите произвольный текст: ")
slovo = input("Введите слово для поиска: ")
kolvo = text.count(slovo)
fi = text.find(slovo)
bez = text.replace(slovo, "")
print("Количество встреченных слов:", kolvo)
if fi != -1:
    print("Индекс первого встреченного слова:", fi)
else:
    print("Слово не найдено в тексте")
print("Текст без введенного слова:",bez)