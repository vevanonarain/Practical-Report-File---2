#Task 39 - 1/12/2022
#Vevan O Narain S6-C

"""WAPP to read a string and display the following pattern if the string is 'INDIA'."""
"""TASK 39-B:
        I
      I N
    I N D
  I N D I
I N D I A"""

for i in range(len(n)):
    print(" " * (len(n) - i - 1), end=n[0:i + 1])
    print()