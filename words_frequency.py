import string
def words_frequency():
    #getting a text document from the user
    file_name = input("Enter the file name to open: ") 
    #checking whether its a valid document that can be opened
    try:
        file_words = open(file_name)
    #if it is invalid returning an error message to the user and exiting the block
    except:
        print("File cannot be opened:", file_name)
        exit()

    word_count = dict()
    #iterating through every line/sentence in the text document
    for line in file_words:
        print(line)
        #the methods below remove the punctuation in the words
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        #splitting the line/sentence into word list
        words = line.split()
        #iterating through every word in the words that make up each sentence
        for word in words:
            #checking whether the word already exists in the word_count dictionary and if not set its initial count to 1 otherwise increament it by 1
            # if word not in word_count:
            #     word_count[word] = 1
            # else:
            #     word_count[word] += 1
        #alternative syntax that would get rid of if...else block but instead use get()
            word_count[word] = word_count.get(word, 0) + 1
    #printing words which appear more than twice
    for key in word_count:
        if word_count[key] >= 2:
            print(key, word_count[key])

#printing a dictionary of words and their frequency
    print(word_count)

words_frequency()
