colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "голубой": (0, 255, 255),
    "пурпурный": (255, 0, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0)
}
color1 = "красный"
color2 = "синий"
r1, g1, b1 = colors[color1]
r2, g2, b2 = colors[color2]
mix = (
    (r1 + r2) // 2,
    (g1 + g2) // 2,
    (b1 + b2) // 2
)
print(f"Смешиваем {color1} {colors[color1]} и {color2} {colors[color2]}")
print(f"Полученный цвет: {mix}")
color_to_invert = "зеленый"
r, g, b = colors[color_to_invert]
invert = (255 - r, 255 - g, 255 - b)
print(f"Инвертируем {color_to_invert} {colors[color_to_invert]}")
print(f"Инвертированный цвет: {invert}")
print("Все цвета в палитре:")
for color_name, rgb in colors.items():
    print(f"{color_name}: {rgb}")