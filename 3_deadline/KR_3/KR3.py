# Функция-генератор для чисел Фибоначчи
def fibonacci_gen(n):
    """Генерирует n чисел Фибоначчи"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Класс для анализа последовательностей
class SequenceAnalyzer:
    """Анализатор числовых последовательностей"""
    
    def get_even_numbers(self, generator):
        """Возвращает список четных чисел из генератора"""
        result = []
        for number in generator:
            if number % 2 == 0:  # Проверяем четность
                result.append(number)
        return result


# Демонстрация работы
if __name__ == "__main__":
    
    # Создаем генератор для 10 чисел Фибоначчи
    gen = fibonacci_gen(10)
    
    # Выводим все сгенерированные числа
    print("Первые 10 чисел Фибоначчи:")
    for num in fibonacci_gen(10):
        print(f"  {num}", end=" ")
    print()
    
    # Создаем анализатор
    analyzer = SequenceAnalyzer()
    
    # Создаем новый генератор
    gen_new = fibonacci_gen(10)
    
    # Получаем четные числа
    even_numbers = analyzer.get_even_numbers(gen_new)
    
    # Выводим результат
    print(f"\nЧетные числа из последовательности: {even_numbers}")
    
    # Дополнительная проверка
    print("\nПроверка работы:")
    print(f"Количество четных чисел: {len(even_numbers)}")
    
    # Подробный вывод
    print("\nПодробно:")
    fib_list = list(fibonacci_gen(10))
    print(f"Все числа: {fib_list}")
    print(f"Четные: {even_numbers}")