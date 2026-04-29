def make_matrix(key, alphabet):
    c = 0
    i = 0
    j = 0
    a = [[0] * 5 for x in range(5)]
    while i < 5:
        j = 0
        while j < 5:
            a[i][j] = key[c]
            c += 1
            j += 1
            if(c >= len(key)):
                break
        if(c >= len(key)):
            break
        i += 1

    
    c = 0
    did_it_change = True    #I made this so i can tell if i added element in that place or not
    while i < 5:
        while j < 5:
            if alphabet[c] not in key:
                a[i][j] = alphabet[c]
                j += 1
            else:
                did_it_change = False
            c += 1
        if(did_it_change == True):
            i += 1
            j = 0
        else:
            did_it_change = True  
    return a

def prepare_sentence(sentence_input):
    sentence = []
    i = 0

    while i < len(sentence_input) - 1:
        if(sentence_input[i] == sentence_input[i + 1]):
            sentence_input.insert(i + 1, 'x')
        i += 2

    if len(sentence_input) % 2 != 0:
        sentence_input += 'x'

    for i in range(0,len(sentence_input) - 1,2):
        sentence.append(sentence_input[i] + sentence_input[i + 1])
    return sentence
    
def find_pos(a, ch):
    for row in range(5):
        for col in range(5):
            if a[row][col] == ch:
                return [row, col]

def cipher(sentence, a):
    ciphered_sentence = ""
    for i in sentence:
        row1 = find_pos(a, i[0])[0]
        col1 = find_pos(a, i[0])[1]
        row2 = find_pos(a, i[1])[0]
        col2 = find_pos(a, i[1])[1]
        if(row1 == row2):
            ciphered_sentence += a[row1][(col1 + 1) % 5] + a[row2][(col2 + 1) % 5]
        elif(col1 == col2):
            ciphered_sentence += a[(row1 + 1) % 5][col1] + a[(row2 + 1) % 5][col2]
        else:
            ciphered_sentence += a[row1][col2] + a[row2][col1]
    return ciphered_sentence

def decipher(sentence, a):
    deciphered_sentence = ""
    for i in sentence:
        row1 = find_pos(a, i[0])[0]
        col1 = find_pos(a, i[0])[1]
        row2 = find_pos(a, i[1])[0]
        col2 = find_pos(a, i[1])[1]
        if(row1 == row2):
            deciphered_sentence += a[row1][col1 - 1] + a[row2][col2 - 1]
        elif(col1 == col2):
            deciphered_sentence += a[row1 - 1][col1] + a[row2 - 1][col2]
        else:
            deciphered_sentence += a[row1][col2] + a[row2][col1]
    return deciphered_sentence

key_input = input("Enter the key: ").lower()
sentence_input = list(input("Enter the input to cipher or dichiper: ").lower())
sentence = prepare_sentence(sentence_input)
key = ""
for i in key_input:
    if i not in key:
        key += i
if(key.find('j') == -1):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
else:
    alphabet = "abcdefghjklmnopqrstuvwxyz"
a = make_matrix(key, alphabet)
print("Matrix is: ", a)
print("Ciphered text: ", cipher(sentence, a))
print("Deciphered text: ", decipher(sentence, a))
