#Tal Rogozinski
#2/8/2022 
# Word game with three levels: 
# level one is fruits leel 
# two is animals and level 
# three is Computer Parts
from modulefinder import IMPORT_NAME
import random, os
os.system('cls')

def menu():
    print("#############################################################")
    print("#############################################################")
    print("##########-------- Word Guessing Game -----------############")
    print("#####-- First type of word you can guess are fruits --#######")
    print("###--- Second type of word we guess are animals ---##########")
    print("###-- Third type of word we can guess is Computer Parts --###")
    print("################### ARE YOU READY TO PLAY ###################")
    print("#############################################################")
   
    
    print(" What Category will you chose: Fruits, Animals, or Computerparts")

menu()



Fruits=["mango", "bananas", "watermelon", "papaya", "oranges", "strawberries", "apples", "blackberriew", "cantalope", "blueberries", "tangerine"]
Animals = ["elephant", "kangaroo", "lion", "crab", "lizard", "snake", "deer", "toocan", "reindeer", "panda", "fox", "owl"]
Computerparts= ["mouse", "keyboard", "motherboard", "power button", "screen"]

def level():
    global randy
    check = True
    while check:
        userchoice = input("What category would you like?: ")
        if userchoice == "fruits":
            print("cool!")
            randy = random.choice(Fruits)
            check = False
        elif userchoice == "animals":
            print("sweet!")
            randy = random.choice(Animals)
            check = False
        elif userchoice == " parts":
            print(" niceeee")
            randy = random.choice(Computerparts)
            check = False
        else:
            print("ONLY FRUITS, ANIMALS, or COMPPARTS")

level()

guess=""
def guessingFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("please choose enter a letter for the mystery word: ")
            if guess.isalpha() and len(guess)==1:
                check=False
        except:
            if len(guess) >1:
                print("You must choose a singular letter")



def restartgame():
    score = len(randy)*1
    global tries, letterGuessed
    print("--------------------------------------------------------------------------------------")
    print("-----your  score is", score, "would you like to play again? --------------------------")
    print("--------------------------------------------------------------------------------------")
    userinput = input("[yes or no]")
    if userinput == "yes":
        ("The categories are: Fruits, Animals, and COmputer parts")
        print("\n")
        level()
        tries=0
        letterGuessed = ""
    if userinput == "no":
        print(score)
        print("ok goodbye")
        quit()

gameOn=True
tries=0
letterGuessed = ""
while gameOn:
    guessingFunction()
    letterGuessed += guess 
    if guess not in randy:
        tries +=1
        print(tries) 
    countLetter=0
    for letter in randy:
        if letter in letterGuessed:
            print(letter, end= " ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries > 6:
        print("\n you have run out of chances to bad so sad \n")
        restartgame()
        
    if countLetter == len(randy):
        print("CONGRATS YOU GUESSED ALL THE LETERS OF THE WORD :)")
        restartgame()





   
 

    
























































































































































































































































































































































































































































































































































































































































































































































































































