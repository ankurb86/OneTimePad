import sys
import random

#Generating a new key with a length of the Secruity Parameter in bits
def generateNewKey(lambdaVal):
    secretKey = ""
    if(lambdaVal>=1 or lambdaVal<=128):
        for i in range(0,lambdaVal):
            secretKey = secretKey+str(random.randrange(0,2))
        print("The new Secret Key is: ",secretKey)

        #Saving the secret key in the newkey file
        fSecretKey = open("../data/newkey.txt","w")
        fSecretKey.write(secretKey)
        fSecretKey.close()

    else:
        print("The values must be between 1 and 128")


generateNewKey(int(sys.argv[1]))
