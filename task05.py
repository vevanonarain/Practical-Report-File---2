# Task 05 - 4/11/2022
# Vevan O Narain, S6-C

""" Define a function isPrime(N) to check whether N is a prime or not. If prime, the function should
    return 1 otherwise 0. Using the defined function, write a program to display all prime numbers
    between 1 and 100."""
    
def prime(n):
    l = []
    
    for i in range(2, n):
        if n % i == 0:
            l.append(i)
            
    if len(l) > 0:
        return 0
    else:
        return 1
    
x = int(input("Enter Number: "))
print(prime(x))

for i in range(1, 101):
    if prime(i) == 1:
        print(i, end = ', ')