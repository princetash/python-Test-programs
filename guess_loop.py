import random

min = 1
max = 20
number = random.randint(min, max)
attempts = 2

guess = int(input(f"Guess a number from {min, max}: "))

while guess != number:
    if guess < number:
        print("Your number was too low")
    else:
        print("Your number was too high")
    guess = int(input("Please try again: "))
print(f"Congratulations! You guessed correct. The number was {number}")