#FIrst we must make a menu
#define rock paper sciccor in relation to an integer
# define which wins and how
# create option to continue playing if you tie, win or wrong
# loop game fully if player wins
# randomize the answer

import os,random
os.system('cls')

def menu():
    print("############################################################################################")
    print("#                                    Welcome                                               #")
    print("#                   ARE YOU READY TO PLAY ROCK.....PAPER.....SCISSORS                      #")
    print("#                                                                                          #")
    print("# :0  :0     :0     :0    :0     :0    :0     :0     :0     :0    ;0     :0      :0     :0 #")
    print("############################################################################################")
menu()

userchoice = input("Rock, Paper, or Scissors ?:  ")
while userchoice != "Rock" and userchoice != "Scissors" and userchoice != "Paper":
    userchoice = input("Try again you must choose Rock Paper or Scissors:  ")
    ()


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
        print("YOU HAVE TIED")
    elif correctchoice == "Rock":
        print("YOU LOST :(")
    elif correctchoice == "Paper":
        print("YOU WON ;)")






