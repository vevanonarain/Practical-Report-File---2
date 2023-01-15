#Task 25 - 10/11/2022
#Vevan O Narain S6-C

""": WAPP to input eclectic consumption (present reading - previous reading) of a house
and calculate total electric bill based on the above table.
Note: Bill upto 200 units is ZERO."""

def bills(units):
    if (units <= 200):
            bill = 0
    elif (units <= 400):
        bill = units * 4.5

    elif (units <= 800):
        bill = units * 6.5

    elif (units <= 1200):
        bill = units * 7

    else:
        bill = units * 7.75

    return bill

n = float(input("Enter the electric units consumed: "))

print(f"Your payable electricity bill is {bills(n)} INR")