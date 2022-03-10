#first let's import random since we will be shuffling
import random, os
os.system('cls')
def createDeck():
    global deck
    deck=[]
    #next, let's start building lists to build the deck
    #NumberCards is the list to hold numbers plus face cards
    numberCards = []
    suits = ['♥',"♦", "♣", "♠️"]
    royals = ["J", "Q", "K", "A"]
        

    #using loops and append to add our content to numberCards :
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the card faces to the base list
    #Create full deck
    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
#you can print the deck here, if you want to see how it looks
createDeck()
print(deck)
player1=[]
player2=[]
counter=0
def shuffleSplit():
    #now let's see the deck!
    global counter
    global player1
    global player2

    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
    #now let's shuffle our deck!
    #Shuffle the deck cards
    random.shuffle(deck)
    # you could print it again here just to see how it shuffle
    #loop to devide the cards to each player
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
shuffleSplit()
print("player1 ",player1)
print()
print("player2 ",player2)
plyr1=0
plyr2=0
def game():
    global plyr1
    global plyr2
    halfDeck=int(len(deck)/2)
    points=1
    temp1=[]
    temp2=[]
        #ask user to hit a key to release cards

    for i in range (0,halfDeck):
        click=input("Press a any key to get cards")
        print("Player 1     Player 2")
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            plyr1 +=points
            points=1
            temp1.append(player1[i])
            temp1.append(player2[i])
        elif player1[i]<player2[i]:
            plyr2 +=points
            points=1
            temp2.append(player1[i])
            temp2.append(player2[i])
        elif player1[i]==player2[i]:
            points+=1
        print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
def winCheck():
    if plyr1>plyr2:
        print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
    elif plyr1<plyr2:
        print("Player two won the game "+str(plyr2)+" to "+str(plyr1))
    else:
        print("It's a tie "+str(plyr1)+" to "+str(plyr2))
game()
winCheck()
