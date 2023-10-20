import random

min_number = 1
max_number = 20
number = random.randint(min_number, max_number)
attempts = 2

print(f"Guess a number from {min_number} to {max_number}:")

for attempt in range(attempts):
    guess = int(input(f"Attempt {attempt + 1}: "))
    
    if guess < number:
        print("Your number is too low.")
    elif guess > number:
        print("Your number is too high.")
    else:
        print(f"Congratulations! You guessed correctly. The number was {number}.")
        break
else:
    print(f"Sorry, you've run out of attempts. The correct number was {number}.")
