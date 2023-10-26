import string

#finding emails in a document
def read_files():
    fname = input("enter the file nmae: ")
    try:
        file = open(fname)
    except:
        print("File cannot be opened")
        exit()

    
    count = 0
    for line in file:
        #print(line)
        line = line.rstrip()
        #line = line.translate(line.maketrans('', '', string.punctuation))
        #line = line.upper()
        #print(line)
        #print(type(line))
        if line.startswith("From "):
            words= line.split()

            for word in words:
                if word.find("@") == -1: continue
                print(word)
                count += 1
    
    print(count)



read_files()