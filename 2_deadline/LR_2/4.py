n = int(input("Введите высоту пирамиды: "))
for a in range(1, n + 1):
    probely = " " * (n - a)
    vozrast = ""
    for b in range(1, a + 1):
        vozrast += str(b)
    ubyv = ""
    for b in range(a - 1, 0, -1):
        ubyv += str(b)
    print(probely + vozrast + ubyv)