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
myNumber=random.randint(1,10)
print("################################################################")
print("#                                                              #")
print("# Guess a Number Menu  #") 
print ("Welcome to the NUMBER GAME :))")     
print(' choose a game! ')
print ('')
print ('choose 1 for 1-10.')
print ('choose 2 for 1-50')
print ('choose 3 for 1-100')


GameOn=True
while(GameOn):
    userGuess=int(input("Guess a number from 1-10 "))
    if myNumber ==userGuess:
        print("You guessed it!!!")
        GameOn=False
    else:
        print("better luck next time:((")
print("The number to guess was "+ str(myNumber))
