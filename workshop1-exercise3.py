import statistics as stat

string1 = input("Insert a string\n")

print("String length: %s, de string is: %s" % (len(string1),string1))

string2 = input("insert another string\t")
integer1 = int(input("insert an integer\t"))

#for i in range(0,integer1):
#    print(string2,end="")
print(string2*integer1)

print(string2[0:2]*integer1)

int1 = 50
int2 = 8
int3 = 16

print(sorted([int1,int2,int3]))