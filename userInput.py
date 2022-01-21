import os, random
os.system('cls')


print("___________________________________")
print("                                   ")
print("        Guess a Number Menu        ")
print("                                   ")
print("  Option #1 Random between 1-10    ")
print("  Option #1 Random between 1-50    ")
print("  Option #1 Random between 1-100   ")
print("___________________________________")
difficulty=int(input("Input 1 for option 1, 2 for option 2, and 3 for option 3: "))
if difficulty==1:
    myNumber =random.randint(1,10)
    guess=int(input("Guess a number between 1 and 10 "))
    if guess == myNumber:
                print("Victory")
    else:
        while guess != myNumber:
            if guess < myNumber:
                guess=int(input("Your guess was too low, please guess again: "))
            elif guess > myNumber:
                guess=int(input("Your guess was too high, please guess again: "))
    print("Victory")
elif difficulty==2:
    myNumber =random.randint(1,50)
    guess=int(input("Guess a number between 1 and 50 "))
    if guess == myNumber:
                print("Victory")
    else:
        while guess != myNumber:
            if guess < myNumber:
                guess=int(input("Your guess was too low, please guess again: "))
            elif guess > myNumber:
                guess=int(input("Your guess was too high, please guess again: "))
    print("Victory")
elif difficulty==3:
    myNumber =random.randint(1,100)
    guess=int(input("Guess a number between 1 and 100 "))
    if guess == myNumber:
                print("Victory")
    else:
        while guess != myNumber:
            if guess < myNumber:
                guess=int(input("Your guess was too low, please guess again: "))
            elif guess > myNumber:
                guess=int(input("Your guess was too high, please guess again: "))
    print("Victory")
else:
    print("You Have Discovered the Secret Difficulty \n\n\t Prepare Yourself", end='\n\n')
    myNumber =random.randint(1,1000)
    guess=int(input("Guess a number between 1 and 1000 "))
    if guess == myNumber:
                print("Victory")
    else:
        while guess != myNumber:
            if guess < myNumber:
                guess=int(input("Your guess was too low, please guess again: "))
            elif guess > myNumber:
                guess=int(input("Your guess was too high, please guess again: "))
    print("Victory")