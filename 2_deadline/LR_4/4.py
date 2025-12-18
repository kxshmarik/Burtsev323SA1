import random
temperatures = [random.randint(10, 25) for _ in range(14)]
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)
vishesr = sum(1 for temp in temperatures if temp > avg_temp)
sorted_temps = sorted(temperatures)
fahrenheit_temps = [temp * 9/5 + 32 for temp in temperatures]
print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp:.1f}°C")
print(f"Дней выше средней: {vishesr}")
print(f"Отсортированные температуры: {sorted_temps}")
print(f"Температуры в Фаренгейтах: {[f'{temp:.1f}°F' for temp in fahrenheit_temps]}")