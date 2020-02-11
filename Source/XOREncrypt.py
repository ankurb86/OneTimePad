#Function to find xor values of 2 Binary strings and return a Binary number in string format
def XORStrings(string1, string2):
    string3=''
    for i in range(0, len(string1)):
        if(string1[i]==string2[i]):
            #string3 = '0' + string3
            string3 = string3 + '0'
            #print('Character at string1: ',string1[:i+1],'\nCharacter at string2: ',string2[:i+1],'\nCharacter at string3',string3)
        else:
            #string3 = '1' + string3
            string3 = string3 + '1'
            #print('Character at string1: ', string1[:i+1], '\nCharacter at string2: ', string2[:i+1],'\nCharacter at string3', string3)
    return string3
