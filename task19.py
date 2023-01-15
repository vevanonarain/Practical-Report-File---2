#Task 19 - 9/11/2022
#Vevan O Narain S6-C

"""Define a function to read a name and display the initials as M.K.G"""

def name(str):
    x = str.split()
    l = []

    for i in x:
        initials = i[0]
        l.append(initials)

    print(*l, sep = '.')

string= input("Enter Name: ")
name(string)