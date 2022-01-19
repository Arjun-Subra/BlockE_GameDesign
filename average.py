import os
#Arjun Subramanian
# Jan 14, 2022
# Declare variables, print variables, print type of data, 
# learn some operators

# this symbol is for comments means the computer will ignore.
# I want to clear my terminal
os.system('cls')
#Program is Average of three tests

#Declare and assign values
test1=89
test2=78.5
test3=86
Flag=False

#to display things on the screen we use the function print()
# print(type(test1), type(test2), type(Flag))

#declare Sum to add
Sum=test1+test2+test3
Average=Sum/3
print(Average)




print("Test1 =", test1,end=" ")
print("Test =", test2)
print("The average of 3 tests is", Average)