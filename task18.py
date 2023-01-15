#Task 18 - 9/11/2022
#Vevan O Narain S6-C

"""Define functions Pow(X,N) and Factorial(N) to calculate and return XN and N! respectively.
Using the defined function, write programs to calculate and display the sum of following series:
x + x^2/2! - x^3/3! + x^4/4!... x^n/n!."""

def factorial(v):
    if v == 0 or v == 1:
        return 1
    return v * factorial(v - 1)

def series(n, x):
    sum = x
    for i in range(2, n + 1):
        term = ((-1 ** i) * (x ** i))/factorial(i)
        sum += term
        
    return term

a = int(input("Enter n: "))
b = int(input("Enter x: "))

print(series(a, b))