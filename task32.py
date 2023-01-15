#Task 32 - 12/11/2022
#Vevan O Narain S6-C

"""Define a function FREQTable(T) which accepts a Tuple T, having few natural numbers. The
function creates a Dictionary FT to store the frequency table of individual numbers in the Tuple
T. Function finally returns the Dictionary FT.
If T=(4,2,6,2,4,2,4,2)
The function should return FT={4:3,2:4,6:1}
Write a minimal program to use the defined function effectively"""

d = {}
t = ()

for i in range(10):
    x = (input("Enter Number: "))
    t = t + (x,)

for i in t:
    d[i] = t.count(i)

print(d)