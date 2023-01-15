#Task 30 - 11/11/2022
#Vevan O Narain S6-C

""" Write a Python program to replace last value of tuples in a list"""

def rem(tuples):
    tup = list(tuples)
    tup.pop()
    return tuple(tup)

t = ()

for i in range(10):
    s = input("Enter value: ")
    t = t + (s,)

print(t)
print(rem(t))