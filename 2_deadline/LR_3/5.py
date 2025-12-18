import string
print("Введите текст (пустая строка для завершения):")
text_lines = []
while True:
    line = input()
    if line == "":
        break
    text_lines.append(line)
full_text = " ".join(text_lines)
for punct in string.punctuation:
    full_text = full_text.replace(punct, "")
words = full_text.lower().split()
stat = {}
for word in words:
    if word in stat:
        stat[word] += 1
    else:
        stat[word] = 1
print("Статистика слов:")
print(stat)