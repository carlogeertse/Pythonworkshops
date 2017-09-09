import random

number = random.randint(1, 9)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 9\t"))

print("You guessed right!")