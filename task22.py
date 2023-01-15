#Task 22 - 9/11/2022
#Vevan O Narain S6-C

"""Define a function to input a natural number and display the SUM OF all its DIGITS"""

def sum_dig(n):
    l = []
    for i in str(n):
        l.append(int(i))

    return sum(l)

num = int(input("Enter Number: "))
print(sum_dig(num))