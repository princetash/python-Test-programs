alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Enter a string to encrypt: ").upper()
keys = int(input("Enter a number as the key between 1-25: "))

encrypted_message = ""

for character in message:
    index = alphabet.find(character)
    new_index = index + keys
    #encrypted_message = encrypted_message + alphabet[new_index]
    if character in alphabet:
        encrypted_message = encrypted_message + alphabet[new_index]
    else:
        encrypted_message = encrypted_message + character
print("Encrypted message is:", encrypted_message)