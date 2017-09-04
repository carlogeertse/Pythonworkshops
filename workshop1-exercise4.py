import math
import random

radius = int(input("Please insert the radius of a cricle:\t"))

print(math.pi * radius ** 2)

name = input("Please insert your name:\t")

print(" ".join(name[::-1]))

#number = random.randint(1, 9)
#guess = 0
#while guess != number:
#    guess = int(input("Guess a number between 1 and 9\t"))

print("You guessed right!")

for i in range(1,5):
    for j in range (1,3):
        print("*"*(i+j))

