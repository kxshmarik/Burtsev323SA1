def create_counter():
    schetchik = 0
    def count():
        nonlocal schetchik
        schetchik += 1
        return schetchik
    return count
counter = create_counter()
print(counter())
print(counter())
print(counter())