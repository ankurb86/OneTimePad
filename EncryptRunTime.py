import random
from XOREncrypt import XORStrings
import timeit

def evalEncrypt():

    print("***************************************************")
    print("Encryption")
    print("***************************************************")

    avgRunTime = 0
    lambdaVal = 128
    for i in range(0,10):
        startTime = timeit.default_timer()

        #get Message
        fPlainText = open("../data/plaintext.txt", "r")
        plainTextString = fPlainText.read()
        fPlainText.close()

        #Generating the Secret Key:
        secretKey = ''
        for i in range(0, lambdaVal):
            secretKey = secretKey + str(random.randrange(0, 2))

        fSecretKey = open("../data/newkey.txt","w")
        fSecretKey.write(secretKey)
        fSecretKey.close()

        print("The Original message is: ", plainTextString)
        print("The Secret Key is: ", secretKey)
        asciiMessage = ""
        for ascText in plainTextString:
            asciiMessage = asciiMessage + str(ord(ascText))
        print("The ASCII Message is: ", asciiMessage)
        binaryStringValue = '0' + bin(int.from_bytes(plainTextString.encode(), 'big'))[2:].zfill(8)
        print('Binary Message:', binaryStringValue)
        if (secretKey.__len__() == binaryStringValue.__len__()):

            cipherText = XORStrings(binaryStringValue, secretKey)
            print('CipherText : ', cipherText)
            fCipherText = open("../data/ciphertext.txt", "w")
            fCipherText.write(cipherText)
            fCipherText.close()

            stopTime = timeit.default_timer()
            avgRunTime = avgRunTime + (stopTime - startTime)
            print("\nThe run Time of the Encryption Function is: ", stopTime - startTime)



        else:
            open("../data/ciphertext.txt", "w").close()
            print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("ERROR:")
            print("The length of the Message doesn't match that of the Secret Key.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    #divide the sum of the total time of the runs with the No. of runs made to get the Average running time of each run
    avgRunTime = avgRunTime/10
    print("\n\nThe average time that the Encryption Function runs for is: ", avgRunTime)

evalEncrypt()