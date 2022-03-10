import mimetypes
import os
from posixpath import lexists
os.system('cls')
myName="Arjun Subramanian"
myStatement="""My name is 
so nice because
b;ah blah blaggg

what vever
ever"""
print("My last name starts with",myName[6])
if "blah" in myStatement:
    print("true")
print('expert' not in myStatement)

INDEX=myName.find("a")
print(INDEX)
wordLen=len(myName)
print(wordLen)
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i,end=", ")
print("")
print("done")
myStatement=myStatement.upper()
print(myStatement)
letter=input("Dear user, please give us a nice letter ")
print("Thank you, the letter is "+letter)
if letter in myStatement:
    print("GREAT")
