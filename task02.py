# Task 02 - 31/10/22
# Vevan O Narain S6-C


"""Write Python programs to input a natural number N (if N=4) and display the following PATTERNS:
   *
  ***
 *****
*******
"""

def numbers(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * ((2 * i) - 1))

x = int(input("Enter Number: "))
                
numbers(x)