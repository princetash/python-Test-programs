"""Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number."""

def numbers():
    npt = input("Enter a number: ")
    count = 1
    total = 0
    average = 0
    while npt != "done":
        try:
            npt = input("Enter a number: ")
            inpt = int(npt)
            total = total + inpt
            for _ in npt:
                count += 1
            average = total / count
        except:
            if npt == "done":
                break
            else:
                print("Invalid Value")
                continue    
    
            
    print(total)
    print(count)
    print(average)
numbers()