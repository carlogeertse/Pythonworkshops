def print_pascal_triangle(lines=5):
    list1 = []
    for i in range(0, lines):
        list1.append([])
    line_length = 1
    for i in range(0, lines):
        list1[i].append(1)
        if line_length > 1:
            if line_length > 2:
                for j in range(0, line_length-2):
                    list1[i].append(list1[i-1][j]+list1[i-1][j+1])
            list1[i].append(1)
        line_length += 1
    return list1

pascallist = print_pascal_triangle(8)
space_amount = len(pascallist)
for line in pascallist:
    print("\t"*space_amount,end="")
    for number in line:
        print(number,end="\t\t")
    print("")
    space_amount -= 1