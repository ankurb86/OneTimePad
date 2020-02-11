import random

def findFrequency():
    lambdaVal = 3
    secretKey = ""
    for i in range(0, lambdaVal):
        secretKey = secretKey + str(random.randrange(0, 2))
    print("The new Secret Key is: ", secretKey.encode("utf-8").decode("ascii"))

    secretKeyList = [secretKey]
    for r in range(0, 5001):
        secretKey = ''
        for i in range(0, lambdaVal):
            secretKey = secretKey + str(random.randrange(0, 2))
        print("Current Run: ", r, "The new Secret Key is: ", secretKey.encode("utf-8").decode("ascii"))
        secretKeyList.append(secretKey.encode("utf-8").decode("ascii"))

    secretKeyList.sort()
    from itertools import groupby
    print("\nKeys\tFrequencies\n----------------")
    for key,group in groupby(secretKeyList):
        print(key,"\t",len(list(group)))


findFrequency()
