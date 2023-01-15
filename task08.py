# Task 08 - 2/11/2022
# Vevan O Narain, S6-C

""" Define a function SumOfFactors(N) to calculate and return sum of all proper factors of N (all
    factors including 1 and excluding the number N itself). Using the defined function, write a
    program to check whether 2 numbers A and B are amicable or not."""
    
def sumOfFactors(n):
    l = []
    
    for i in range(1,  n):
        if n % i == 0:
            l.append(i)
            
    return sum(l)

x = int(input("Enter Number: "))
print(sumOfFactors(x))

y = int(input("Enter Number 1: "))
z = int(input("Enter Number 2: "))

if sumOfFactors(z) == y and sumOfFactors(y) == z:
    print(f"{y} and {z} are amicable numbers")
else:
    print(f"{y} and {z} are not amicable numbers")