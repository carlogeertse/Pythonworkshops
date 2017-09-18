import copy

list1 = [1, 2, 3, 4, 9, 5, 6, 2, 2, 3, 4, 1, 9, 10]

list2 = list(set(list1))  # If order is not important
print(list2)

# If order is important
list3 = copy.deepcopy(list1)
i = 0
seen = []
while i < len(list3):
    if list3[i] in seen:
        list3.pop(i)
        i -= 1
    seen.append(list3[i])
    i += 1

print(list3)