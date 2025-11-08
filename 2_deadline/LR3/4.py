products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
max_sold = max(products.items(), key=lambda x: x[1]["sold"])
print(f"Самый продаваемый товар: {max_sold[0]} ({max_sold[1]['sold']} шт.)")
all = 0
for product, info in products.items():
    viruchka = info["price"] * info["sold"]
    all += viruchka
    products[product]["revenue"] = viruchka
print(f"Общая выручка магазина: {all} руб.")
max_revenue = max(products.items(), key=lambda x: x[1]["revenue"])
print(f"Товар с наибольшей выручкой: {max_revenue[0]} ({max_revenue[1]['revenue']} руб.)")