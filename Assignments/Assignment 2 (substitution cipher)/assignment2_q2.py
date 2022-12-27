# dictionary to store the letters
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# their substitution mapping
key = "QWERTYUIOP ZXCVBNMASDFGHJKL"


# encrypt function
def encText(text):
    print("\n---Started enciphering---\n")
    cipher = ""
    # looping though plain text
    for char in text:
        # changing the lower case to upper case
        # keeping encrypted text in upper and plain/decrypted text in lower
        char = char.upper()
        # finding the character in the key string which maps to the plain text
        cipher += key[LETTERS.find(char)]

    print("\n---Ended enciphering---\n")
    return cipher


def decText(cipher):
    print("\n---Started deciphering---\n")
    dcipher = ""
    # looping through the cipher text single char at a time
    for char in cipher:
        # finding the character in the Letters string which maps to the key string
        dcipher += LETTERS[key.find(char)]
    # changing the deciphered text back to lower case
    print("\n---Ended deciphering---\n")
    return dcipher.lower()

# open a file in read mode with the plain text
while True:   
# repeat until the try statement succeeds
    try:
        file = open("C:\\Users\\sachl\\Desktop\\plaintext_assignment2.ssc", "r")
        print("\nFile open successfully!")
        break
        # exit the loop
    except IOError:
        input("Could not open file!")
        # restart the loop

print("\nPlain text read from file:")
# reading the whole file
plain = file.read()
print(plain)

# calling encryption function
cipher = encText(plain)
print("\nCipher text is:")
print(cipher)

# calling the decryption function
dcipher = decText(cipher)
print("\nThe original plain text is:")
print(dcipher,"\n")

# closing the file
file.close()