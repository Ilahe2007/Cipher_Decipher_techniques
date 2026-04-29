BlockSize = 4
#this function ciphers the text without ecb
def Ceasar_cipher(txt, key):
    cipher_txt = ""

    for i in txt:
        if(i.isalpha() == True):
            if(i.upper() == i):                               
                pos = (ord(i) - 65 + key) % 26 + 65           #65 is A 
            else:
                pos = (ord(i) - 97 + key) % 26 + 97           #97 is a
            i = chr(pos)                                      
        cipher_txt += i                                          
    return cipher_txt                                         
                                                              
#this function deciphers the text without ecb                       
def Ceasar_decipher(txt, key):                                
    decipher_txt = ""                                         
                                                                                                                      
    for i in txt:                                             
        if(i.isalpha() == True):                           
            if(i.upper() == i):                             
                pos = (ord(i) - 65 - key) % 26 + 65
            else:
                pos = (ord(i) - 97 - key) % 26 + 97
            i = chr(pos)
        decipher_txt += i
    return decipher_txt

def add_padding(txt):
    remainder = len(txt) % BlockSize
    #i wrote this, so if the block isn't enough to be equal to other block sizes then we add # as padding so we have same blocksize, but if it is equal to like perfectly needed size then size - size = 0 so there will be no additional padding needed
    padding_size = BlockSize - remainder    
    return txt + ('#' * padding_size)


def ECB_cipher(txt, key):
    padded = add_padding(txt)
    result = ""
    #each block gets ciphered and added to result
    for i in range(0, len(padded), BlockSize):
        block = padded[i: (i + BlockSize)] #from i to i + BlockSize
        result += Ceasar_cipher(block, key)
    return result

#for after the decipher I won't need the padding
def strip_padding(txt):
    return txt.rstrip('#')

def ECB_decipher(txt, key):
    result = ""
    #for each block I discipher and collect into result
    for i in range(0, len(txt), BlockSize):
        block = txt[i: (i + BlockSize)]   #from i to i + BlockSize
        result += Ceasar_decipher(block, key)
    return strip_padding(result)


txt = input("Enter the text: ")
key = int(input("Enter the key: "))

operation = 0
while(operation != 1 and operation != 2):
    operation = int(input("Enter 1 for cipher, 2 for decipher: "))
    if operation == 1:
        #padding will be printed here because I want to let user know where the text ends
        print(ECB_cipher(txt, key))
    elif operation == 2:
        #this shows original text after decipher so no need for padding to printed
        print(ECB_decipher(txt, key))
    else:
        print("This isn't a valid input")
