from functools import reduce

# Print square of numbers from 1 till 10 by using map
print(list(map(lambda x: x*x, range(1,11))))

# Print square of even numbers from 1 till 10 by using map and filter
print(list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, range(1,11)))))

# Print all even numbers between 1 and 20 by using filter
print(list(filter(lambda x: x % 2 == 0, range (1,21))))

# Print all squares of the numbers between 1 and 20 by using map
print(list(map(lambda x: x*x, range(1,21))))

# Print the maximum number from a list using reduce
numbers = [-1,-5,14,15,6,7,2,5,65,2,2,87,56,-10,43,12,35,7,8,8,43,19,9,8,-40]
numbers2 = range(1,11)
print(reduce(max,numbers))

# Print the sum of the number from 1 to 100 using reduce
print(reduce(lambda x,y: x + y,range(1,101)))

# Print the total product of the numbers from 1 to 50 using reduce
print(reduce(lambda x,y: x*y,range(1,50)))

# Print all positive numbers from a list using filter
print(list(filter(lambda x: x>=0, numbers)))

# Find all elements that exist in list 1 and list 2
print(list(filter(lambda x: x in numbers2,numbers)))