#Tal Rogozinski
#Objective = rock paper scissors game
#steps:
#1-make a menu
#2-define rock paper and scissors in numerical values
#3-randomize the code
#4-make a while loop where it defines what to enter and if it does not enter that certian choice make it an "error" not an actula one tho
#5- define which wins how
#6-create option to continue playing if you tie, win or wrong
#7-loop game fully/ give player anothe rchnce


import os,random
os.system('cls')
userchoice= " "
def menu():
    global userchoice
    print("############################################################################################")
    print("#                                    Welcome                                               #")
    print("#                   ARE YOU READY TO PLAY ROCK.....PAPER.....SCISSORS                      #")
    print("#                                                                                          #")
    print("# :0  :0     :0     :0    :0     :0    :0     :0     :0     :0    ;0     :0      :0     :0 #")
    print("############################################################################################")
    userchoice = input("Rock, Paper, or Scissors ?:  ")
    while userchoice != "Rock" and userchoice != "Scissors" and userchoice != "Paper":
        userchoice = input("Try again you must choose Rock Paper or Scissors:  ")
        ()
menu()

GameOn = True
while GameOn:
    randomnum = random.randint(0,2)
    if randomnum ==0:
        correctchoice = "Rock" 
    elif randomnum ==1:
        correctchoice = "Paper"
    elif randomnum ==2:
        correctchoice = "Scissors"

    print("Your chose: ", userchoice)
    print("The correct choice was: ", correctchoice)
    if userchoice == "Rock":
        if correctchoice == "Rock":
            print("YOU HAVE TIED")
        elif correctchoice == "Paper":
            print("YOU LOST :(")
        elif correctchoice == "Scissors":
            print("YOU WON ;)")
    if userchoice == "Paper":
        if correctchoice == "Paper":
            print("YOU HAVE TIED")
        elif correctchoice == "Scissors":
            print("YOU LOST :(")
        elif correctchoice == "Rock":
            print("YOU WON ;)")
    if userchoice == "Scissors":

        if correctchoice == "Scissors":
            print("You HAVE TIED")
        elif correctchoice == "Rock":
            print("YOU LOST :(")

        elif correctchoice == "Paper":
            print("YOU WON ;)")
    userchoice = input(" WOuld you like to play again [YA OR NAW]")
    if "Y" in userchoice:
        # os.system('cls')
        menu()
    else:
        print(" quitter ")
        quit()







