import binascii
from XOREncrypt import XORStrings
import timeit
import os.path
import sys

def Enc():
    #Start time to record when the execution begins
    startTime = timeit.default_timer()

    print("***************************************************")
    print("Encryption")
    print("***************************************************")

    #Retrieve Message
    fPlainText = open("../data/plaintext.txt","r")
    plainTextString = fPlainText.read()
    fPlainText.close()

    #Retrieve Secret Key
    fSecretKey = open("../data/key.txt","r")
    secretKey = fSecretKey.read()
    fSecretKey.close()

    print("The Original message is: ", plainTextString)
    print("The Secret Key is: ",secretKey)
    # Convert text to ASCII Value
    asciiMessage=""
    for ascText in plainTextString:
        asciiMessage = asciiMessage + str(ord(ascText))
    print("The ASCII Message is: ",asciiMessage)

    #Convert ASCII to Binary Value
    binaryStringValue = '0' + bin(int.from_bytes(plainTextString.encode(), 'big'))[2:].zfill(8)
    print('Binary Message:', binaryStringValue)

    #Check if length of Secret Key equals the Binary Message String
    if(secretKey.__len__() == binaryStringValue.__len__()):

        #xor the binary message string with the secret key to get the ciphertext
        cipherText = XORStrings(binaryStringValue, secretKey)
        print('CipherText : ', cipherText)

        #Save the Ciphertext in the file
        fCipherText = open("../data/ciphertext.txt", "w")
        fCipherText.write(cipherText)
        fCipherText.close()

        #Check Execution time using the startTime variable
        stopTime = timeit.default_timer()
        print("\nThe run Time of the Encryption Function is: ", stopTime - startTime)

        return cipherText
    else:
        #If Lengths are not equal, then clear the ciphertext in the file
        cipherText = ""
        open("../data/ciphertext.txt","w").close()
        print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("ERROR:")
        print("The length of the Message doesn't match that of the Secret Key.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return cipherText

Enc()
