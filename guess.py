def guessing_game(attempts_left):
    number = 60  # the value of the original number
    guess = int(input("Guess a number! "))

    if guess == number:
        print(
            f"Congratulations! You guessed correctly. The number was {number}")
    else:
        if attempts_left > 1:
            if guess > number:
                print(f"{guess} is too high.")
            else:
                print(f"{guess} is too low.")
            print(
                f"You have {attempts_left - 1} {'attempts' if attempts_left > 2 else 'attempt'} left.")
            guessing_game(attempts_left - 1)
        else:
            print(f"Sorry, you're out of attempts. The number was {number}")


print("Welcome to the Guessing Game!")
print("You have 5 attempts to guess the number.")

guessing_game(5)  # Start the game with 5 attempts
