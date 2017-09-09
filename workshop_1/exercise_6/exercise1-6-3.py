list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def get_item_at_second_index(tuple1):
    return tuple1[1]


list2 = sorted(list1, key=get_item_at_second_index)
print(list2)
