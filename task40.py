# Task 40 - 1/12/2022
# Vevan O Narain S6- C

""" Write a Python program to read a string and check whether the string is a
    palindrome or not (with or without case sensitivity). """

str = input("Enter a string: ")

if (str.lower() == str.lower()[::-1]):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")