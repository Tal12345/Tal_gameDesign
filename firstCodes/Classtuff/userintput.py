# Tal Rogozinski
#01/21/22

#We are going to learn the input() function, random numbers
# type casting, branching, looping
import os, random 
os.system('cls')
#declare variable fpr user input
# print("enter a number from 1-10 ", end=" ")
# userinfo=int(input()) #input returns a string we must tupe cast if we need a number
# print("The number is %.2f " %(userinfo/3))
# guess=int(input("Please give me a number "))

#guess a number
#myNumber = 9 instead of using a fixed number we will use a random
#Lets make menu a funcion key word def
myNumber=0
def menu():
    print("-----------------------------------------------------------------")
    print("-                           WELCOME                             -")   
    print("-                      Guess a Number Game                      -")
    print("-                                                               -")
    print("-                        Level 1 = 1-10                         -")
    print("-                        Level 2 = 1-50                         -")
    print("-                        Level 3 = 1-100                        -")
    print("-                       Select Your Level                       -")
    print("-----------------------------------------------------------------")
#Checking for correct user input
menu()
check=True
while check:
    try:
        level=int(input("Level: "))
        check= False
    except ValueError:
        print("Sorry thats not a level, please enter 1 to 3 only!")

    
if level == 1:
    myNumber= random.randint(1,10)
elif level == 2:
    myNumber= random.randint(1,50)
elif level == 3:
    myNumber= random.randint(1,100)
print(level)

GameOn=True
while(GameOn):
    userGuess=int(input("Give me a number: "))
    if myNumber ==userGuess:
        print("You guessed it!!!")
        GameOn=False
    else:
        print("better luck next time:(( the number was", myNumber)
print("The number to guess was "+ str(myNumber))
os.system('cls')
menu()







