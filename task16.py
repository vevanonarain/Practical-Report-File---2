#Task 16 - 8/11/2022
#Vevan O Narain S6-C

"""Define functions Pow(X,N) and Factorial(N) to calculate and return XN and N! respectively.
Using the defined function, write programs to calculate and display the sum of following series:
1 - x + x^2 - x^3 + x^4... x^n."""

def series(n, x):
    sum = 0
    for i in range(0, n + 1):
        term = (-1 ** i) * (x ** i)
        sum += term
        
    return term

a = int(input("Enter n: "))
b = int(input("Enter x: "))

print(series(a, b))