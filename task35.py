#Task 35 - 12/11/2022
#Vevan O Narain S6-C

"""Write a program to remove duplicate values from a dictionary"""

d = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}

print("The original dictionary is : " + str(d))
  
temp = []
res = dict()
for key, val in d.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
 
print("The dictionary after values removal : " + str(res)) 