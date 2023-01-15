# Task 03 - 2/11/2022
# Vevan O Narain, S6-C

"""Define a function isArmstrong(N) to check whether N is a Armstrong or not. If Armstrong, the
   function should return 1 otherwise 0. Using the defined function, write a program to display all
   Armstrong numbers between 1 and 1000."""

def armstrong(n):
    s = str(n)
    l = []
    c = []
    
    for i in range(len(s)):
        l.append(int(s[i]))
    
    for i in l:
        cube = i ** 3
        c.append(cube)
        
    if sum(c) == n:
        return 1
    else:
        return 0
    
x = int(input("Enter Number: "))
print(armstrong(x))

print("Armstrong Numbers between 1 and 1000 are: ")

for j in range(1, 1001):
    if armstrong(j) == 1:
        print(j, end = ', ')