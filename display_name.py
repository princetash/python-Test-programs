
# part 1
def display_left_chars(name, n):
    if n >= 0 and n <= len(name):
        result = name[:n]
        print(result)
        return result
    else:
        print(f"n is greater than the length of the name '{name}'")


name = input("Enter your name: ")
n = int(input("Enter an integer for n: "))

display_left_chars(name, n)


# part 2


def vowels_count(name):
    vowels = 'aeiou'
    count = 0
    for character in name:
        if character in vowels:
            count += 1
    return count


name = input("Enter your name: ").lower()
num_vowels = vowels_count(name)
print(f"Number of vowels in your name: {num_vowels}")


# part 3
def reverse_name(name):
    reversed_name = name[::-1]
    return reversed_name


name = input("Enter your name: ")
reversed_name = reverse_name(name)
print(f"Reversed name: {reversed_name}")


# combined functions
def manipulate_name(name, operation):
    if operation == "display":
        n = int(input("Enter an integer for n: "))
        if 0 <= n <= len(name):
            result = name[:n]
            print(result)
        else:
            print(f"n is greater than the length of the name '{name}'")
    elif operation == "count":
        vowels = 'aeiouAEIOU'
        count = sum(1 for char in name if char in vowels)
        print(f"Number of vowels in your name: {count}")
    elif operation == "reverse":
        reversed_name = name[::-1]
        print(f"Reversed name: {reversed_name}")
    else:
        print("Invalid operation")


name = input("Enter your name: ")
operation = input("Enter the operation (display/count/reverse): ").lower()
manipulate_name(name, operation)
