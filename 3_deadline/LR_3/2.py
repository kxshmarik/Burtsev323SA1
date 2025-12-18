def sum_digits(number: int) -> int:
    # Если число меньше 10, возвращаем само число
    if number < 10:
        return number
    
    # Сумма цифр = последняя цифра + сумма цифр оставшегося числа
    return (number % 10) + sum_digits(number // 10)

# Примеры использования
print("Сумма цифр 12345:", sum_digits(12345))
print("Сумма цифр 9876:", sum_digits(9876))
print("Сумма цифр 100:", sum_digits(100))
print("Сумма цифр 0:", sum_digits(0))