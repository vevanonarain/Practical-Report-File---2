#Task 10 - 7/11/2022
#Vevan O Narain S6-C

"""Define a recursive function Factorial(N) to calculate and return factorial of N. Write a program
to display factorial of the first 5 natural numbers."""

def factorial(v):
    if v == 0 or v == 1:
        return 1
    return v * factorial(v - 1)

for i in range(1, 6):
    print(factorial(i))