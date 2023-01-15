#Task 24 - 10/11/2022
#Vevan O Narain S6-C

"""WAPP to read a year and check whether the year is a Leap year or not"""

def leap(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if leap(n) == True:
    print("Year is a leap year.")
else:
    print("Year is not a leap year.")