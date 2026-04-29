#this function ciphers the text
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
                                                              
#this function deciphers the text                             
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

txt = input("Enter the text: ")
key = int(input("Enter the key: "))
operation = 0
while(operation != 1 and operation != 2):
    operation = int(input("Enter 1 for cipher, 2 for decipher: "))
    if operation == 1:
        print(Ceasar_cipher(txt, key))
    elif operation == 2:
        print(Ceasar_decipher(txt, key))
    else:
        print("This isn't a valid input")
