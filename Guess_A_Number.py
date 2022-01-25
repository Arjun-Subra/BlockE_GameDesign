import os, random
from turtle import color
os.system('cls')

def menu():
    print("___________________________________")
    print("                                   ")
    print("        Guess a Number Menu        ")
    print("                                   ")
    print("  Option #1 Random between 1-10    ")
    print("  Option #1 Random between 1-50    ")
    print("  Option #1 Random between 1-100   ")
    print("___________________________________")

cont="y"

while cont=="y":
    menu()
    try:
        difficulty=int(input("Input 1 for option 1, 2 for option 2, and 3 for option 3: "))

    except ValueError:
        print("You Have Discovered the Super Secret Difficulty \n\n\t You did this to youself by trying to break my code.", end='\n\n')
        myNumber =random.randint(1,1000000)
        guess=int(input("Guess a number between 1 and 1000000 "))
        if guess == myNumber:
            print("You have completed your punishment.")
            cont=input("Do you want to play again? If yes type y if no type n: ")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
        print("You have completed your punishment.")
        cont=input("Do you want to play normally now? If yes type y if no type n: ")

    if difficulty==1:
        myNumber =random.randint(1,10)
        guess=int(input("Guess a number between 1 and 10 "))
        if guess == myNumber:
                    print("Victory")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
        print("Victory")
        cont=input("Do you want to play again? If yes type y if no type n: ")

    elif difficulty==2:
        myNumber =random.randint(1,50)
        guess=int(input("Guess a number between 1 and 50 "))
        if guess == myNumber:
                    print("Victory")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
        print("Victory")
        cont=input("Do you want to play again? If yes type y if no type n: ")
        if cont == "y":
            print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")

    elif difficulty==3:
        myNumber =random.randint(1,100)
        guess=int(input("Guess a number between 1 and 100 "))
        if guess == myNumber:
                    print("Victory")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
        print("Victory")
        cont=input("Do you want to play again? If yes type y if no type n: ")
        if cont == "y":
            print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")

    else:
        print("You Have Discovered the Secret Difficulty \n\n\t Prepare Yourself", end='\n\n')
        myNumber =random.randint(1,1000)
        guess=int(input("Guess a number between 1 and 1000 "))
        if guess == myNumber:
                    print("Victory")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
        print("Victory")
        cont=input("Do you want to play again? If yes type y if no type n: ")
