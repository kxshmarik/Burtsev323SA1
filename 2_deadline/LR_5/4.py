text = input("Введите текст: ").lower()
words = text.split()
uniq = set(words)
print(f"Уникальные слова: {len(uniq)}")
long = {word for word in uniq if len(word) > 5}
print(f"Длинные слова: {long}")
key = "python" in uniq or "programming" in uniq
print(f"Найдены ключевые слова: {key}")
print(f"Все уникальные слова: {uniq}")