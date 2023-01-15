# Task 01 - 30/10/2022
# Vevan O Narain, S6-C

""" Define a function Pattern(N) to display the following pattern when N=4:
   1
  212
 32123
4321234
Write a program to display this pattern for N=5""" 
    
def numbers(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end = '')
        
        for j in range(1, i + 1):
            print(j, end = '')
            
        for k in range(i - 1, 0, -1):
            print(k, end = '')
            
        print()

x = int(input("Enter Number: "))
                
numbers(x)