#make a while loop from now
#Menu
#ask user for rock,paper,or scissors
#generate random number between 1-3 for computer's choice
#if statement for each user option
#3 if statements inside each user if for each possible cpu choice
#


import os,random

cont="y"

while cont=="y":
    Game=True
    os.system('cls')
    print("______________________________")
    print("|                            |")
    print("|         Welcome To         |")
    print("|    Rock, Paper, Scissors   |")
    print("|____________________________|")

    user=input("To pick rock type \"r\", to pick paper type \"p\", and to pick scissors type \"s\"")
    cpu=random.randint(1,3)
    while Game:
        if user == "r":
            if cpu == 1:
                user=input("Draw, the cpu also choose rock. Please pick again. To pick rock type \"r\", to pick paper type \"p\", and to pick scissors type \"s\"")
            elif cpu == 2:
                print("The cpu choose paper. You Lose")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
            elif cpu == 3:
                print("The cpu choose scissors, You Win")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
        elif user == "p":
            if cpu == 1:
                print("The cpu choose rock, You Win")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
            elif cpu == 2:
                user=input("Draw, the cpu also choose paper. Please pick again. To pick rock type \"r\", to pick paper type \"p\", and to pick scissors type \"s\"")
            elif cpu == 3:
                print("The cpu choose scissors. You Lose")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
        elif user == "s":
            if cpu == 1:
                print("The cpu choose rock. You Lose")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
            elif cpu == 2:
                print("The cpu choose paper, You Win")
                cont=input("Do you want to play again? If yes type \"y\" if no type \"n\"")
                Game=False
            elif cpu == 3:
                user=input("Draw, the cpu also choose scissors. Please pick again. To pick rock type \"r\", to pick paper type \"p\", and to pick scissors type \"s\"")
        else:
            print("That is not a valid choice Please choose again.")
            Game = False
            os.system('cls')