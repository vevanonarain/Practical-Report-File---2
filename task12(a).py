# Task 12 - 7/11/2022
# Vevan O Narain S6-C

"""Define a function Encode(W) which encode a word (group of characters) as follows:
i) Lower case alphabets are changed into upper case alphabets and vice versa.
Characters other than alphabets remains unchanged.
ii) First character is swapped with the second character, third with the fourth character,
and so on. In case of odd number of characters, last character remains unchanged.
Write program which will read a sentence from the user and display the encrypted sentence
after encoding all words."""

#Part-1

def encode():
    
    w = input("Enter String: ")
    l = []

    for i in range(len(w)):
        if w[i].isupper():
            l.append(w[i].lower())
        elif w[i].islower():
            l.append(w[i].upper())
    
    print(*l, sep = '')

encode()