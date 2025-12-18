def find_max(a, b):
    if a > b:
        return a
    else:
        return b
max_num = find_max(101, 25)
print(max_num)
print(find_max(52, 42))
print(find_max(-5, 10))
print(find_max(7, 7))