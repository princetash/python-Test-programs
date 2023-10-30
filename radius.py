# Part 1


def print_circum(radius):
    pi = 3.14159
    circumference = pi * 2 * radius
    print("The radius of the circle is:", radius)
    print("Circumference of the circle:", circumference)


# call 1:
# getting the first radius from the user
radius1 = float(input("Enter the radius: "))
print_circum(radius1)
# Call 2:
# getting the second radius from the user
radius2 = float(input("Enter the radius: "))
print_circum(radius2)
# Call 3:
# getting the third radius from the user
radius3 = float(input("Enter the radius: "))
print_circum(radius3)

"""The program illustrates function definition and usage where the code defines `princt_circum` which calculates the circumference of a circle by taking radius as an input. The user input is a numerical value and it converts it into floating point number to avoid errors. If the int data type is used in the user input instead of float, it would raise a ValueError if the user attempted to input a floating value for the radius. Another feature illustrated in the program is reusability where the function is only defined once but it is called several times with different radii. In addition, the program incorporates comments which promotes code maintanability and readability. There is also string formatting in the print_circum function. This illustrates how to format strings in python and also display numerical values dynamically """
