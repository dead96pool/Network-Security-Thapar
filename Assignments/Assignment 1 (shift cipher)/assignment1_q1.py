# Shift cipher | Caesar cipher
# User input plain text

MAX_KEY_SIZE = 26

def getText():
    print("\nEnter the plain text:")
    return input()

def getKey():
    print("\nEnter the Key (1-%s):" %(MAX_KEY_SIZE))
    key = int(input())
    #check if key in range
    if (key >= 1 and key <= (MAX_KEY_SIZE)):
        return key
    else:
        print("Enter between 1-%s" %(MAX_KEY_SIZE))

def encText(text,k):
    print("\n---Started enciphering---")
# function to encrypt the plain text
# plain text and the key as arguments
    
    # empty string to add a character with each loop
    cipher = ""
    
    for char in text:
        # looping through the length of the plain text taking each letter at a time
        if(char == " "):
            cipher += " "
        elif(char.isupper()):
            # for upper case letters
            cipher += chr( (((ord(char) - 65) + k ) % 26 ) + 65 )
            # shifting the letter by adding the key to the ASCII
            # subtracting 65 to keep letters in the range of 0 -25 | mod26 to keep the sum in the A-Z ASCII 
        elif(char.islower()):
            # for lower case letters
            cipher += chr( (((ord(char) - 97) + k ) % 26 ) + 97 )
    print("\n---Ended enciphering---")
    return cipher


def decText(text):
# function to decrypt the cipher text
# brute forcing the key
    print("\n---Started deciphering---")

    for dkey in range(MAX_KEY_SIZE):
        dcipher = ""
        
        for char in text:
            if(char == " "):
                dcipher += " "
            elif(char.isupper()):
                dcipher += chr((((ord(char) - 65) - dkey) % 26 ) + 65 )
            elif(char.islower()):
                dcipher += chr((((ord(char) - 97) - dkey) % 26 ) + 97 )


        print("Key#"+str(dkey)+" ",dcipher)
        # checking to see if the decrypted text is the same as the plain text given
        if (dcipher == plain):
            print("\n---Ended deciphering---\n")
            return (dcipher, dkey)

    
# user input for plain text and the key | without spaces
plain = getText()
key = getKey()


# calling the encryption function
cipher = encText(plain,key)
print("\nCipher text is:")
print(cipher,"\n")


# calling the decryption function
(dcipher, dkey) = decText(cipher)
print("\nThe Original Plain text is:")
print(dcipher)
print("\nThe key used is:")
print(dkey)
