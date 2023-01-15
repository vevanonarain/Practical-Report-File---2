# Task 13 - 8/11/2022
# Vevan O Narain S6-C

"""Define a function isPalindrome(W) to check whether W is a Palindromic word or not.
Create a List SENTENCES of 5 sentences entered by the users. Using the defined function,
display all Palindromic words present in the 5 sentences.
"""

def isPalindrome():
    l = []
    pallin = []
    not_palllin = []

    for i in range(5):
        w = input("Enter String: ")
        l.append(w)

    for i in l:
        if i == i[::-1]:
            pallin.append(i)
        else:
            not_palllin.append(i)

    print(f"Pallindrome sentence: {pallin}")
    print(f"Non-Pallindrome Sentence: {not_palllin}")

isPalindrome()