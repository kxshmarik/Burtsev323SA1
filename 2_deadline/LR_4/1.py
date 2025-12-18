grades = []
grades.append(5)
grades.append(4)
grades.append(3)
grades.append(5)
grades.append(2)
print(f"Текущие оценки: {grades}")
del grades[0]
grades.pop()
sr = sum(grades) / len(grades)
print(f"Средний балл: {sr}")
print(f"Итоговые оценки: {grades}")