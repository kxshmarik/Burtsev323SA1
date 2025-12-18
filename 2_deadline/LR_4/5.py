import string
text = input("Введите текст: ")
for punct in string.punctuation:
    text = text.replace(punct, '')
words = text.lower().split()
if not words:
    print("Текст не содержит слов!")
else:
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    avg = sum(len(word) for word in words) / len(words)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"Самое длинное слово: '{longest_word}'")
    print(f"Самое короткое слово: '{shortest_word}'")
    print(f"Средняя длина слова: {avg:.1f}")
    print(f"Топ 5 слов: {top_words}")