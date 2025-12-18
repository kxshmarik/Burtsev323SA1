def power(a: float, n: int) -> float:
    # Любое число в степени 0 равно 1
    if n == 0:
        return 1
    
    # a^n = a * a^(n-1)
    return a * power(a, n - 1)

# Примеры использования
print("2^3 =", power(2, 3))
print("5^0 =", power(5, 0))
print("3^4 =", power(3, 4))
print("10^2 =", power(10, 2))