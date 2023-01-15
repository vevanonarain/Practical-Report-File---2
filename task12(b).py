# Task 12 - 7/11/2022
# Vevan O Narain S6-C

"""Define a function Encode(W) which encode a word (group of characters) as follows:
i) Lower case alphabets are changed into upper case alphabets and vice versa.
Characters other than alphabets remains unchanged.
ii) First character is swapped with the second character, third with the fourth character,
and so on. In case of odd number of characters, last character remains unchanged.
Write program which will read a sentence from the user and display the encrypted sentence
after encoding all words."""

#Part-2

def encode():
    
    w = input("Enter String: ")
    l = []

    if len(w) % 2 == 0:
        for i in range(0, len(w), 2):
            l.append(w[i + 1])
            l.append(w[i])
    else:
        for i in range(0, len(w) - 1, 2):
            l.append(w[i + 1])
            l.append(w[i])
        
        l.append(w[-1])
        
        
    print(*l, sep = '')

encode()