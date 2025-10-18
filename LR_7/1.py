napravlenie = input("Введите направление (left, right, straight, back): ")
if napravlenie == "left":
    print("Иду влево")
elif napravlenie == "right":
    print("Иду вправо")
elif napravlenie == "straight":
    print("Иду прямо")
elif napravlenie == "back":
    print("Иду назад")
else:
    print("Неправильное направление")