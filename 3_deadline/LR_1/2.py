def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

# Возвращает текст приветствия
@make_bold
def get_text():
    return "Hello, World!"
print(get_text())

# Другой пример использования
@make_bold
def get_ru_text():
    return "Привет, мир!"
print(get_ru_text())