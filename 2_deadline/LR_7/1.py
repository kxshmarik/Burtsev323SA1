def sum_numbers(*numbers: float) -> float:
    """
    Вычисляет сумму произвольного количества чисел.
    
    Args:
        *numbers (float): Произвольное количество числовых аргументов.
    
    Returns:
        float: Сумма всех переданных чисел.
    """
    return sum(numbers)
print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10.5, 20.3, 30.7))
print(sum_numbers(1, 2))
print(sum_numbers())