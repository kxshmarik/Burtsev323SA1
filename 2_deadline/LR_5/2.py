students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Ашот", 20, 4.1),
    ("Александр", 23, 4.6)
]
print("Студенты старше 20 лет:")
for name, age, avg in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {avg}")
best_student = max(students, key=lambda x: x[2])
print(f"Лучший студент: {best_student[0]}, средний балл: {best_student[2]}")
sorted_students = sorted(students, key=lambda x: x[0])
print("Отсортированный список студентов по имени:")
for name, age, avg in sorted_students:
    print(f"- {name}, {age} лет, средний балл: {avg}")