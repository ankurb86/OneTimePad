from XOREncrypt import XORStrings

def Dec():
    print("\n\n***************************************************")
    print("Decryption")
    print("***************************************************")

    #Retrieve Secret Key
    fSecretKey = open("../data/key.txt","r")
    secretKey = fSecretKey.read()
    fSecretKey.close()

    #Retrieve CipherText
    fCipherText = open("../data/ciphertext.txt","r")
    cipherText = fCipherText.read()
    fCipherText.close()

    if (secretKey.__len__() == cipherText.__len__()):
        #xor the ciphertext with secretkey
        decMessage = XORStrings(cipherText, secretKey)
        print("The Secret Key is: ", secretKey)
        print("The Ciphertext is: ", cipherText)
        print('The deciphered bitStream is: ', decMessage)
        #Convert Binary code to ASCII value
        decodedAsciiMessage = int(decMessage, 2)
        print("Message in ASCII is: ", decodedAsciiMessage)
        #convert ASCII to text
        plainText = decodedAsciiMessage.to_bytes((decodedAsciiMessage.bit_length() + 7) // 8, 'big').decode()
        print("Here is your Message: ", plainText)
        #Save the text in the result file
        fPlainText = open("../data/result.txt", "w")
        fPlainText.write(plainText)
        fPlainText.close()
    else:
        print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("ERROR:")
        print("The length of the CipherText doesn't match that of the Secret Key.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

Dec()