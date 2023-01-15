#Task 49 - 11/1/2023
#Vevan O Narain S6-C

"""WAPP to sort this list in descending order of numbers"""

l = []
for i in range(5):
    x = int(input("Enter Numbers: "))
    l.append(x)

l.sort()

print(l[::-1])