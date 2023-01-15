#Task 21 - 9/11/2022
#Vevan O Narain S6-C

""" WAPP to input a natural number and display the MULTIPLICATION TABLE of that number."""

def multiplication(n):
    for i in range(1, 21):
        print(f"{n} * {i} = {n*i}")

num = int(input("Enter Number: "))
multiplication(num)