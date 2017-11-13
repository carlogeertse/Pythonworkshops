from functools import reduce

print(list(map(lambda x: x*x, range(1,11))))

print(list(filter(lambda x: x % 2 == 0, map(lambda x: x*x, range(1,11)))))

print(list(filter(lambda x: x % 2 == 0, range (1,21))))

print(list(map(lambda x: x*x, range(1,21))))

numbers = [-1,-5,14,15,6,7,2,5,65,2,2,87,56,-10,43,12,35,7,8,8,43,19,9,8,-40]
numbers2 = range(1,11)
print(reduce(max,numbers))

print(reduce(lambda x,y: x + y,range(1,101)))

print(reduce(lambda x,y: x*y,range(1,50)))

print(list(filter(lambda x: x<=0, numbers)))

print(list(filter(lambda x: x in numbers2,numbers)))