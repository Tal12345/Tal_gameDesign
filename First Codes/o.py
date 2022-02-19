#Tal Rogozinski
#2/18/2022
#Create War Game 

import random, os

os.system('cls')
deck=[]

numberCards = []
suits = ['h',"d", "c", "s"]
royals = ["J", "Q", "K", "A"]


for i in range(2,11):
    numberCards.append(str(i))

for j in range(4):
    numberCards.append(royals[j])


for k in range(4):   # four suits
    for l in range(13):
        card = (numberCards[l] + " " + suits[k])
        deck.append(card)

print(deck)

counter=0
for row in range(4):
    for col in range(13):
        print(deck[counter], end=" ")
        counter +=1
    print()


random.shuffle(deck)
player1=[]
player2=[]

for l in range(52):
    if l%2==0:
        player1.append(deck[l])
    else:
        player2.append(deck[l])

print("player1 ",player1)
print()
print("player2 ",player2)
halfDeck=int(len(deck)/2)
plyr1=0
plyr2=0

for i in range (0,halfDeck):
    click=input("Press a any key to get cards: ")
    print("Player 1     Player 2")
    print("     "+player1[i]+"      "+player2[i])

    if player1[i]>player2[i]:
        plyr1 +=1
    elif player1[i]<player2[i]:
        plyr2 +=1
    elif player1[i]==player2[i]:
        player1+=0
    print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
    



if plyr1>plyr2:
    print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
else:
    print("Player two won the game "+str(plyr2)+" to "+str(plyr1))