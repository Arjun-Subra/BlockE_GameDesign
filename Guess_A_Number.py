from ctypes.wintypes import RGB
import os, random
from turtle import color
os.system('cls')

def menu():
    print("___________________________________")
    print("|                                 |")
    print("|       Guess a Number Menu       |")
    print("|                                 |")
    print("| Option #1 Random between 1-10   |")
    print("| Option #1 Random between 1-50   |")
    print("| Option #1 Random between 1-100  |")
    print("|_________________________________|")
Attempts=0

cont="y"

while cont=="y":
    os.system('cls')
    Attempts=0
    menu()
    try:
        difficulty=int(input("Input 1 for option 1, 2 for option 2, and 3 for option 3: "))

    except ValueError:
        os.system('cls')
        print("\n\t\tYou Have Discovered Your Punishment  \n\n\t You did this to youself by trying to break my code.", end='\n\n')
        myNumber =random.randint(1,1000000)
        guess=int(input("Guess a number between 1 and 1000000 "))
        Attempts=Attempts+1
        if guess == myNumber:
            print("Your punishment is over.")
            cont=input("Do you want to play again? If yes type y if no type n: ")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
                    Attempts=Attempts+1
                elif guess > myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                    Attempts=Attempts+1
        print("Your punishment is over.")
        print("It took you", Attempts,"guesses to guest the right number.")
        cont=input("Do you want to play normally now? If yes type y if no type n: ")

    if difficulty==1:
        os.system('cls')
        myNumber =random.randint(1,10)
        guess=int(input("Guess a number between 1 and 10 "))
        Attempts=Attempts+1
        if guess == myNumber:
                    print("Victory")
                    print("It took you", Attempts,"guesses to guest the right number.")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                    Attempts=Attempts+1
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
                    Attempts=Attempts+1
        print("Victory")
        print("It took you", Attempts,"guesses to guest the right number.")
        cont=input("Do you want to play again? If yes type y if no type n: ")

    elif difficulty==2:
        os.system('cls')
        myNumber =random.randint(1,50)
        guess=int(input("Guess a number between 1 and 50 "))
        Attempts=Attempts+1
        if guess == myNumber:
                    print("Victory")
                    print("It took you", Attempts,"guesses to guest the right number.")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                    Attempts=Attempts+1
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
                    Attempts=Attempts+1
        print("Victory")
        print("It took you", Attempts,"guesses to guest the right number.")
        cont=input("Do you want to play again? If yes type y if no type n: ")
        if cont == "y":
            print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")

    elif difficulty==3:
        os.system('cls')
        myNumber =random.randint(1,100)
        guess=int(input("Guess a number between 1 and 100 "))
        Attempts=Attempts+1
        if guess == myNumber:
                    print("Victory")
                    print("It took you", Attempts,"guesses to guest the right number.")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
                    if cont == "y":
                        print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                    Attempts=Attempts+1
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
                    Attempts=Attempts+1
        print("Victory")
        print("It took you", Attempts,"guesses to guest the right number.")
        cont=input("Do you want to play again? If yes type y if no type n: ")
        if cont == "y":
            print("If you want to try a secret difficulty input a number that is not 1, 2, or 3, when you are given the choice again")

    else:
        os.system('cls')
        print("You Have Discovered the Secret Difficulty \n\n\t Prepare Yourself", end='\n\n')
        myNumber =random.randint(1,1000)
        guess=int(input("Guess a number between 1 and 1000 "))
        Attempts=Attempts+1
        if guess == myNumber:
                    print("Victory")
                    print("It took you", Attempts,"guesses to guest the right number.")
                    cont=input("Do you want to play again? If yes type y if no type n: ")
        else:
            while guess != myNumber:
                if guess < myNumber:
                    guess=int(input("Your guess was too low, please guess again: "))
                    Attempts=Attempts+1
                elif guess > myNumber:
                    guess=int(input("Your guess was too high, please guess again: "))
                    Attempts=Attempts+1
        print("Victory")
        print("It took you", Attempts,"guesses to guest the right number.")
        cont=input("Do you want to play again? If yes type y if no type n: ")

print("\n\n\t\tCreated By: DOOM_MASTE\n\n")
