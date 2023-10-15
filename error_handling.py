# Prompt the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Check if both inputs are valid numbers
if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)

    # Check if the second number is zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        # Perform the division operation
        result = num1 / num2
        print(f"Result of division: {result}")
else:
    print("Error: Please enter valid numeric inputs.")

"""I first check if both num1 and num2 are valid numeric inputs using isdigit() which is an inbuilt method found in python. This is to get rid of errors if the user enters a string in the prompt. If they are valid numbers, I proceed with converting them to floats incase the user enters a float value. I then use a conditional statement to check if num2 is zero before attempting the division. If num2 is zero, we print an error message that handles the ZeroDivisionError. Otherwise, we perform the division and display the result.This approach checks for valid inputs and the division by zero scenario using conditional statements. However this method is not preferred since does not handle all possible cases such as when the input is a negative number. Python has an inbuilt try block that checks for errors and raises them. The method uses except blocks to catch specific exceptions such as ValueError for invalid input such as entering text instead of a number """

"""To include more errors it would be preferable to use try-except as shown below """
# Prompt the user to enter two numbers
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Attempt to convert input to float
try:
    num1 = float(num1_str)
    num2 = float(num2_str)

    # Check if the second number is zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        # Perform the division operation
        result = num1 / num2
        print(f"Result of division: {result}")

except ValueError:
    print("Error: Please enter valid numeric inputs.")

"""num1_str and num2_str are strings that store the user's input for the first and second numbers, respectively. Inside a try block, the code attempts to convert num1_str and num2_str to floating-point numbers using float(). This step may raise a ValueError if the input strings cannot be converted to valid floating-point numbers for instance if the user enters non-numeric characters. If the conversion is successful meaning no ValueError is raised, the code proceeds to the next step. It checks if num2 (the second number) is equal to zero. If num2 is zero, it prints an error message indicating that division by zero is not allowed. If num2 is not zero, it calculates the result of the division operation num1 / num2 and stores it in the variable result. Finally, it prints the result of the division operation if everything went smoothly. If a ValueError occurs during the conversion of the input strings to floats such as if the user enters invalid non-numeric input, it catches the exception in the except ValueError block and prints an error message asking the user to enter valid numeric inputs."""

"""Significance of Error Handling:

Error handling is crucial because it prevents a program from crashing when it encounters unexpected situations. In this division by zero scenario, without error handling, the program would crash, causing a poor user experience. Error handling allows us to gracefully handle errors, display informative messages, and continue program execution or take corrective actions."""
"""Potential Impact of Not Handling Errors:

failure to handle ZeroDivisionError can lead to the program crashing hence can disrupt user experience and leave users with a poor impression of the software.In addition it can cause user frustrations and debugging challenges. When users encounter an error without a clear explanation or resolution, they can become frustrated and may abandon the application or website. Error handling provides a way to guide users and offer solutions or alternatives because without proper error handling, it becomes challenging to diagnose and fix issues. Developers might struggle to identify the source of the problem, leading to longer debugging cycles.

By teaching junior developers about error handling, we empower them to write robust and reliable code that gracefully handles unexpected situations, enhancing the overall quality and resilience of their programs."""

# Prompt the user to enter two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Division operation
    result = num1 / num2

    # Check for division by zero
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    # Output the result
    print(f"Result of division: {result}")

except ValueError as ve:
    print(f"ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

"""We use a try block to handle potential errors like shown above. Inside the try block, we prompt the user to enter two numbers and perform the division operation then introduce a condition that raises a ZeroDivisionError if the second number is zero. We use except blocks to catch specific exceptions such as ValueError for invalid input such as entering text instead of a number, ZeroDivisionError for division by zero and a generic Exception block to catch any unexpected errors. This method uses a special keyword called 'raise'."""
