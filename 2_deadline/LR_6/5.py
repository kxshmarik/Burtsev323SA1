def display_user_profile(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")
    print()
display_user_profile(age=28, name="Иван", city="Москва")
display_user_profile(city="Санкт-Петербург", name="Петр", age=52)
display_user_profile(name="Петр", city="Казань", age=30)