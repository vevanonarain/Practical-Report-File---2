#Task 38 - 1/12/2022
#Vevan O Narain S6-C

"""WAPP to check in a string, to check if a character is a string(lower case/upper case), 
a digit or a special character"""

def char_type(str):
    l = []
    u = []
    d = []
    sc = []

    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(str)):
        if str[i].lower == str[i]:
            l.append(str[i])
        elif str[i].upper == str[i]:
            u.append(str[i])
        elif str[i] in n:
            d.append(str[i])
        else:
            sc.append(str[i])

        return l, u, d, sc

string = input("Enter String: ")
print(char_type(string))