from random import randint
counter = {
    'яблоки': {'max': 20, 'current': 10},
    'бананы': {'max': 15, 'current': 8},
    'апельсины': {'max': 25, 'current': 12},
    'арбузы': {'max': 10, 'current': 5}
}
store = {
    'яблоки': {'max': 100, 'current': 50},
    'бананы': {'max': 80, 'current': 40},
    'апельсины': {'max': 120, 'current': 60},
    'арбузы': {'max': 60, 'current': 30}
}
price = {
    'яблоки': {'sale_price': 50, 'purchase_price': 30},
    'бананы': {'sale_price': 40, 'purchase_price': 25},
    'апельсины': {'sale_price': 60, 'purchase_price': 35},
    'арбузы': {'sale_price': 100, 'purchase_price': 70}
}
money = 1000
day = 1
max_days = 10
print("Добро пожаловать в CRM систему ларька 'АнтиАшот'!")

while day <= max_days and money > 0:
    print(f"=== День {day} ===")
    print(f"Денег: {money} руб.")
    print("На прилавке:")
    for fruit, info in counter.items():
        print(f"  {fruit}: {info['current']}/{info['max']}")
    print("За прилавком:")
    for fruit, info in store.items():
        print(f"  {fruit}: {info['current']}/{info['max']}")
    
    print("Доступные действия:")
    print("1 - Перераспределить фрукты")
    print("2 - Заказать фрукты / Просмотреть актуальные цены")
    print("3 - Закончить день")
    action = input("Выбрано действие: ")
    
    if action == '1':
        fruit = input("Какой фрукт перераспределить? ")
        if fruit in counter:
            amount = int(input(f"Сколько {fruit} переместить (отрицательное = убрать с прилавка)? "))
            if amount > 0:
                if store[fruit]['current'] >= amount:
                    if counter[fruit]['current'] + amount <= counter[fruit]['max']:
                        store[fruit]['current'] -= amount
                        counter[fruit]['current'] += amount
                        print(f"Добавлено {amount} {fruit} на прилавок")
                    else:
                        print("Не хватает места на прилавке!")
                else:
                    print("Не хватает фруктов за прилавком!")
            else:
                amount = abs(amount)
                if counter[fruit]['current'] >= amount:
                    if store[fruit]['current'] + amount <= store[fruit]['max']:
                        counter[fruit]['current'] -= amount
                        store[fruit]['current'] += amount
                        print(f"Убрано {amount} {fruit} с прилавка")
                    else:
                        print("Не хватает места за прилавком!")
                else:
                    print("Не хватает фруктов на прилавке!")
        else:
            print("Такого фрукта нет! Вы вышли в начальное меню")
    
    elif action == '2':
        print("Актуальные цены за позицию:")                 #ЗАКАЗАТЬ
        for fruit, prices in price.items():
            print(f"  {fruit}: покупка - {prices['purchase_price']} руб., продажа - {prices['sale_price']} руб.")
        fruit = input("Какие фрукты заказать? (Для выхода напишите 0) ")
        if fruit in store:
            amount = int(input(f"Сколько {fruit} заказать? "))
            cost = amount * price[fruit]['purchase_price']
            if money >= cost:
                if store[fruit]['current'] + amount <= store[fruit]['max']:
                    money -= cost
                    store[fruit]['current'] += amount
                    print(f"Заказано {amount} {fruit} за {cost} руб.")
                else:
                    print("Не хватает места для хранения!")
            else:
                print("Недостаточно денег!")
        else:
            print("Такого фрукта нет! Вы вышли в начальное меню")
    
    elif action == '3':
        print("--- Завершение дня ---")
        prodano_segodnya = 0
        for fruit in counter:
            if counter[fruit]['current'] > 0:
                for _ in range(counter[fruit]['current']):
                    if randint(1, 100) <= 30:  # ШАНС ПРОДАЖИ
                        counter[fruit]['current'] -= 1
                        money += price[fruit]['sale_price']
                        prodano_segodnya += 1
        print(f"Сегодня продано {prodano_segodnya} фруктов")
        
        # АШОТ
        if randint(1, 100) <= 20:  # ШАНС КРАЖИ
            stolen_fruit = 'арбузы'
            if counter[stolen_fruit]['current'] > 0:
                stolen_amount = randint(
                    counter[stolen_fruit]['current'] // 2,
                    counter[stolen_fruit]['current']
                )
                counter[stolen_fruit]['current'] -= stolen_amount
                print(f"Ашот Похититель Арбузов украл {stolen_amount} арбузов!")
        
        for fruit in price:
            change = randint(-5, 5)
            price[fruit]['sale_price'] = max(10, price[fruit]['sale_price'] + change)
            price[fruit]['purchase_price'] = max(5, price[fruit]['purchase_price'] + change)
        print("Цены на фрукты изменились")
        day += 1
    else:
        print("Неверное действие!")
        
if money <= 0:
    print("Вы обанкротились! Придется вернуться на арбузные плантации...")
else:
    print(f"Поздравляем! Вы прожили {max_days} дней и пережили Ашота!")
    print("Ашота упаковала полиция и он больше не потревожит ваш ларёк")
    print(f"Ваш финальный капитал: {money} руб.")