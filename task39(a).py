#Task 39 - 1/12/2022
#Vevan O Narain S6-C

"""WAPP to read a string and display the following pattern if the string is 'INDIA'."""
"""TASK 39-A: 
I
I N
I N D
I N D I
I N D I A"""

n = input("Enter a string: ")

if (n == 'INDIA'):
    for i in range(len(n)):
        print(n[0:i + 1])

