# count function
def count_fu(word, l):
    count = 0
    for letter in word:
        if letter == l:
            count += 1
    print(count)


count_fu("jesus", "s")


"""Rewrite the function so that instead of traversing the string, it uses the three parameter version of find from the previous section.
"""

# search function


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("james", "m"))


"""As an exercise, modify find so that it has a third parameter, the index in word where it
should start looking."""

def find(word, letter, start_index):
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# Example usage:
word = "james"
letter = "m"
start_index = 1  # You can specify the starting index here
result = find(word, letter, start_index)
print(result)
