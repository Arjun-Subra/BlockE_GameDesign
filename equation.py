import os
#Arjun Subramanian
#01/19/22

#Objectives: Other operators, exponent, modules format printing escape character


#Program creating and equation, asking user input 
# and formatting the output
os.system('cls')
#Declare Variables
v1=int(input())
v2=int(input())
v3=int(input())
v4=int(input())
# print("\" \t \\")
#Calculate equation
# print(2**4)
result= (3*v1 - 2*(v2)**2/v3)/v4
print("The result of (3 *",v1,"- 2*(",v2,")**2/",v3,")/",v4,"is: %6.2f"%result)