"""Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards."""

#forward printing
fruit = "apple"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


# for letter in fruit:
#     print(letter)


#backward printing
fruit = "apple"
index = len(fruit) - 1  # Start at the last character's index
while index >= 0:  # Loop until the first character's index (0)
    letter = fruit[index]
    print(letter)
    index = index - 1  # Move backwards through the string

