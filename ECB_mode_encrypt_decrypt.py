BlockSize = 4
alphabet = "abcdefghijklmnopqrstuvwxyz"
key_alphabet = "qwertyuiopasdfghjklzxcvbnm"
#this function ciphers the text without ecb using monolit encription
def cipher(txt):
    cipher_txt = ""
    for i in txt:
        if(i.isalpha() == True):
            if(i.upper() == i):                
                i = (key_alphabet[alphabet.find(i.lower())]).upper()
            else:
                i = (key_alphabet[alphabet.find(i)]) 
        elif(i == '\n'):
            i = ' '
        cipher_txt += i                                          
    return cipher_txt                                         
                                                              
#this function deciphers the text without ecb                       
def decipher(txt):                                
    decipher_txt = ""                                         
                                                                                                                      
    for i in txt:                                             
        if(i.isalpha() == True):                           
            if(i.upper() == i):                      
                i = (alphabet[key_alphabet.find(i.lower())]).upper() 
            else:
                i = (alphabet[key_alphabet.find(i)])
        elif(i == '\n'):
            i = ' '
        decipher_txt += i
    return decipher_txt

def add_padding(txt):
    remainder = len(txt) % BlockSize
    #i wrote this, so if the block isn't enough to be equal to other block sizes then we add # as padding so we have same blocksize, but if it is equal to like perfectly needed size then size - size = 0 so there will be no additional padding needed
    if(remainder != 0):
        padding_size = BlockSize - remainder    
    else:
        padding_size = 0
    return txt + ('#' * padding_size)


def ECB_cipher(txt):
    padded = add_padding(txt)
    result = ""
    #each block gets ciphered and added to result
    for i in range(0, len(padded), BlockSize):
        block = padded[i: (i + BlockSize)] #from i to i + BlockSize
        result += cipher(block)
    return result

#for after the decipher I won't need the padding
def strip_padding(txt):
    return txt.rstrip('#')

def ECB_decipher(txt):
    result = ""
    #for each block I discipher and collect into result
    for i in range(0, len(txt), BlockSize):
        block = txt[i: (i + BlockSize)]   #from i to i + BlockSize
        result += decipher(block)
    return strip_padding(result)


operation = 0
operation = int(input("Enter 1 for cipher, 2 for decipher: "))
    
converted_file = open("converted_file.txt","w")
txt = "new"
with open("test.txt", "r", encoding="utf-8-sig") as test_file:
    while txt:
        txt = test_file.read(BlockSize)
        if operation == 1:
            converted_file.write(ECB_cipher(txt))
        elif operation == 2:
            converted_file.write(ECB_decipher(txt))
converted_file.close()
