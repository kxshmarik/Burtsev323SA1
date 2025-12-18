class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        # Складывает два вектора
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # Вычитает один вектор из другого
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        # Умножение вектора на число или скалярное произведение
        if isinstance(other, (int, float)):
            # Умножение на число
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            # Скалярное произведение
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Неподдерживаемый тип для умножения")
    
    def __eq__(self, other):
        # Проверка равенства векторов
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False


# Пример использования
v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(v1)
print(v2)
print(v1 + v2)             # Vector(6, 4)
print(v1 - v2)             # Vector(-2, 2)
print(v1 * 3)              # Vector(6, 9)
print(v1 * v2)             # 11 (2*4 + 3*1)
print(v1 == Vector(2, 3))  # True
print(v1 == Vector(1, 3))  # False