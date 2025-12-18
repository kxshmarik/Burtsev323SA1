def simple_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Ошибка: неизвестный оператор!"
result1 = simple_calculator(10, 2, '*')
print(result1)
result2 = simple_calculator(15, 3, '+')
print(result2)
result3 = simple_calculator(20, 4, '/')
print(result3)
result4 = simple_calculator(25, 5, '-')
print(result4)