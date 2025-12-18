# 1. Функция поиска
def task_1(arr):
    for i in arr:
        if i == 100:
            return True
    return False
# Сложность: O(n) - потому что в худшем случае нужно пройти по всем элементам массива

# 2. Функция доступа
def task_2(arr):
    return arr[0] + arr[-1]
# Сложность: O(1) - доступ к элементам по индексу выполняется за константное время

# 3. Функция пар
def task_3(arr):
    count = 0
    for i in arr:
        for j in arr:
            if i == j:
                count += 1
    return count
# Сложность: O(n^2) - вложенные циклы проходят по всем элементам n*n раз