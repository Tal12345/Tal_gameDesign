#Tal Rogozinski
#2/10/2022 
# Word game with three levels: 
# level one is fruits leel 
# two is animals and level 
# three is Computer Parts
from modulefinder import IMPORT_NAME
import random, os
os.system('cls')
highscore= 0

def menu():
    print("#############################################################")
    print("##########-------- Word Guessing Game -----------############")
    print("#####-------------- Level 1 is fruits -----------------######")
    print("#####-------------- Level 2 is animals -----------------#####")
    print("###----------- Level 3  is Computer Parts ----------------###")
    print("####------------------Leader Board-----------------------####")
    print("#########:) :) ;) : ) ARE YOU READY TO PLAY :):):):):)#######")
    print("#############################################################")
   
    print("What Category will you chose: Fruits, Animals, or Computerparts")
    print ('your score is:',highscore)
menu() 



Fruits=["mango", "bananas", "watermelon", "papaya", "oranges", "strawberries", "apples", "blackberriew", "cantalope", "blueberries", "tangerine"]
Animals = ["elephant", "kangaroo", "lion", "crab", "lizard", "snake", "deer", "toocan", "reindeer", "panda", "fox", "owl"]
Computerparts= ["mouse", "keyboard", "motherboard", "powerbutton", "screen"]


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
        elif userchoice == "computer parts":
            print(" niceeee")
            randy = random.choice(Computerparts)
            check = False
        else:
            print("ONLY FRUITS, ANIMALS, or COMPUTER PARTS")

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


highscore=0

def restart():
    global tries, letterGuessed, highscore
    score = (len(randy)-2*(tries))
    highscore = 0
    if score>highscore: 
        highscore=score
    print("############################################################")
    print("############# The high score is", score, " wanna play again?#")
    print("############################################################")
    print("your  score is", score, "would you like to play again?: ")
    userinput = input("[YA or NO]")
    if userinput == "YA":
        print("The categories are: Fruits, Animals, and Computer parts")
        level()
        tries=0
        letterGuessed = ""
    if userinput == "NO":
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
        restart()
        
    if countLetter == len(randy):
        print("CONGRATS YOU GUESSED ALL THE LETERS OF THE WORD :)")
        restart()

