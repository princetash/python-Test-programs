aliens = 2

password = "ALIENS"

print("Aliens have invaded our land")
print("You need to activate the defense system")
print("Hope you got the guts to do what it takes and the password")
print()
print("-" * 60)
print(" " * 5 + "WELCOME TO THE GLOBAL DEFENCE SYSTEM" + " " *5)
print("-" * 60)

guess = input("Enter the password: " ).upper()
attempts = 2
population = 74000000

while guess != password:
    print()
    print("Incorrect password")
    print()
    aliens = aliens ** 2
    print("Alien population is", aliens , "Try again")
    attempts -= 1
    guess = input("Please enter the password: ").upper()
    if aliens > population:
         print("Oops! The aliens have conqured and outnumbered us")
         break
    elif attempts <= 1:
        print("You have no attempts left")
        break
else:
    print("Hurray! We won and saved the earth")
