#Task 34 - 12/11/2022
#Vevan O Narain S6-C

"""A Python Dictionary - EMP, storing names of few employees as the key(s) with their monthly 
salaries as value(s), working in a Software Development MNC, wimilar to given below assuming 
that the names of the employees are unique.
EMP = {'Manisha': 80000, 'Mariam': 70000, 'Malala': 75000} 
Write a python program to do the following:
    1. Create and display the dictionary, storing 5 items. Input the details from the user.
    2. Display the names of the employees along with their annual salaries. Also, display the
       avarage of the annual salaries.
    3. Compute and display the maximum and minimum of the Monthly salaries of the employees."""

emp = {}

for i in range(5):
    name = input("Enter Name: ")
    sal = int(input("Enter Monthly Salary: "))

    emp[name] = sal

print(f"Dictionary: {emp}")

l = []
n = []

for i in emp:
    l.append(emp[i] * 12)
    n.append(i)

print(f"Names of employees along with their annual salaries are are: ")
for i in range(len(emp)):
    print(f"{i + 1}) {n[i]}:{l[i]}")

print(f"Average of all salaries is: {sum(l)/len(l)}")

print(f"Maximum Monthly Salary: {max(l)/12}")
print(f"Minimum Monthly Salary: {min(l)/12}")