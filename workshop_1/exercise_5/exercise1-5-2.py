string = "The lyrics is not that poor!"

index_not = string.find("not")
index_poor = -1

if index_not != -1:
    index_poor = string[index_not:].find("poor")

if index_poor != -1:
    index_poor += index_not
    print(string[index_not:index_poor])
    string = string.replace(string[index_not:index_poor + 4], "good")

print(string)
