import string


def count_word_occurrences(text, word):
    """
    Counts the occurrences of a specific word in a given text.

    :param text: The text to search for word occurrences.
    :param word: The word to count occurrences of.
    :return: The count of word occurrences in the text.
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    word = word.lower()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


print(count_word_occurrences("This is a 'test'. Test if this works.", "test"))
print(count_word_occurrences("Hello, world!", "WORLD"))
