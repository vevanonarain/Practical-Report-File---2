# Task 04 - 2/11/2022
# Vevan O Narain, S6-C

"""Define a function isPalindrome(N) to check whether N is a Palindromic number or not. If
   Palindrome, the function should return 1 otherwise 0. Using the defined function, write a
   program to display all Palindromic numbers between 1 and 1000."""
   
def pallindrome(n):
    x = str(n)
    
    if x == x[::-1]:
        return 1
    else:
        return 0     
    
x = int(input("Enter Number: "))
print(pallindrome(x))
        
print("Pallindrome Numbers between 1 and 1000 are: ")

for j in range(1, 1001):
    if pallindrome(j) == 1:
        print(j, end = ', ')