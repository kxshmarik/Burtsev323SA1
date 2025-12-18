class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        # Строка вида "Название" (Автор, Год)
        return f'"{self.title}" ({self.author}, {self.year})'
    
    def __repr__(self):
        # Строка, с помощью которой можно пересоздать объект: Book('Title', 'Author', 2020)
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Пример использования
book = Book("1984", "George Orwell", 1949)
print(book)
print(repr(book))