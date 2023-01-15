#Task 20 - 9/11/2022
#Vevan O Narain S6-C

"""Define a function to read a name and display the initials as M.K.Gandhi"""

def name(str):
    x = str.split()
    last = x.pop()
    l = []

    for i in x:
        initials = i[0]
        l.append(initials)

    print(*l, sep = '.', end = '.')
    print(last)

string= input("Enter Name: ")
name(string)