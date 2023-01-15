#Task 29 - 11/11/2022
#Vevan O Narain S6-C

"""Write a Python program to reverse a tuple"""

def Reverse(tuples):
    tup = tuples[::-1]
    return tup

t = ()

for i in range(10):
    s = input("Enter value: ")
    t = t + (s,)

print(t)
print(Reverse(t))