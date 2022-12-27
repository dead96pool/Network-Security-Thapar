

dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,!\"$%^&*(){}[]:;'\|!@#<>?/"
# length 80 [0-79]

MAX_KEY_SIZE = len(dict)

def getPlain():
    print("\nEnter the plain text:")
    return input()

def getKey():
    print("\nEnter the key(1-%s):" %(MAX_KEY_SIZE-1))
    key = int(input())
    if(key >= 1 and key <= MAX_KEY_SIZE-1):
        return key


def encText(plain, key):
    cipher = ""

    for char in plain:
        cipher += dict[ (dict.find(char) + key) %80]

    return cipher


def decText(cipher):
    

    for dkey in range(MAX_KEY_SIZE):
        dcipher = ""

        for char in cipher:
            dcipher += dict[ (dict.find(char) - dkey)%80]
        #print("key",dkey," ",dcipher)

        if (dcipher == plain):
            return (dcipher, dkey)

plain = getPlain()
key = getKey()


cipher = encText(plain,key)
print("\nThe Cipher text is:")
print(cipher)

(dcipher, dkey) = decText(cipher)
print("\nThe Original Plain text is:")
print(dcipher)
print("\nThe key used is:")
print(dkey)
