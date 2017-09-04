stars = 1

for i in range(1, 8):
    for j in range(stars):
        print("*", end="")

    if i > 3:
        stars -= 1
    else:
        stars += 1
    print("")
