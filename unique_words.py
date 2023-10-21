
import string
"""Exercise 4: Find all unique words in a file
Shakespeare used over 20,000 words in his works. But how would you
determine that? How would you produce the list of all the words that
Shakespeare used? Would you download all his work, read it and track
all unique words by hand?
Let’s use Python to achieve that instead. List all unique words, sorted
in alphabetical order, that are stored in a file romeo.txt containing a
subset of Shakespeare’s work.
To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
Create a list of unique words, which will contain the final result. Write
a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For
each word, check to see if the word is already in the list of unique
words. If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words
in alphabetical order"""
#finding unique words using an input

def uniq_words():
    paragraph = input("Enter the sentence: ").lower()
    np = paragraph.split(" ")
    unique_words = []
    for words in np:
        if words.endswith('.'):
            words.strip('.')
            continue
        if words in unique_words:
            continue
        else:
            unique_words.append(words)
    print(sorted(unique_words))
    #print(dir(words))
uniq_words()


#finding unique words from a file
def unique_words_file():
    #requesting for a file from the user
    file_name = input("Enter the file name to open: ")
    #attempting to open the file and if it can't be opened send an error message to the user then exti
    try:
        file_words = open(file_name)
    except:
        print("File cannot be opened:", file_name)
        exit()
    #initializing an empty list of unique words
    unique_words = []
    #iterating through every lion in the document
    for line in file_words:
        print(line)
        #removing punctuation marks in every line
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split(" ")
        #print(words)
        #iterating through every word in all the words that make up the line/sentence
        for word in words:
            #sentence = "" + word
            #print(word)
            #print(sentence, end="---")
            # if word.endswith('.'):
            #     word.strip('.')
            #     continue
            if word in unique_words:
                continue
            else:
                unique_words.append(word)
    print("Length of all words: ", len(words))
    print("Length of sorted unique words: ", len(sorted(unique_words)))
    print()
    print(sorted(unique_words))

unique_words_file()

