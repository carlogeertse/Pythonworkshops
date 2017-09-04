a = 0
b = 1

while a < 50 and b < 50:
    print(max(a, b), end=" ")
    if a < b:
        a = a + b
    else:
        b = a + b
