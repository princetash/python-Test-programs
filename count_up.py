

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


"""In this code, the base case is when n reaches 0 and at this point it will print "Blastoff!" and stop the recursion. If n is not 0, it will print the current value of n then make a recursive call to countup function with n+1 which will increament the value of n. This process will continue untill n reaches 0 and "Blastoff!" is printed. Therefore, when you call countup function with the value of n as -3, it will count up from -3, to 0 and then print "Blastoff!" as expected"""

number = int(input("Enter a number: "))  # Get input from the user
# Determine which function to call based on the input
if number > 0:
    countdown(number)
elif number < 0:
    countup(number)
else:
    countup(number)
"""If the input number is positive, the program calls countdown. This is because we want to count down to zero from the positive number. If the input number is negative, the program calls countup. This is because we want to count up from the negative number to zero. If the input number is zero, we simply print "Blastoff!" since there is no counting needed in this case"""
