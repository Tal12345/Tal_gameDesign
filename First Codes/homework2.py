#Tal Rogozinski
#1/26/2022
#Finishing the Number guess game
from asyncore import loop
import os, random
import numbers 
os.system('cls')

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
# check=True
# while check:
#     try:
#         level=int(input("Level: "))
#         check= False
#     except ValueError:
#         print("Sorry thats not a level, please enter 1 to 3 only!")

def level(dif):

    if level(dif) == 1:
        myNumber= random.randint(1,10)
    elif level(dif) == 2:
        myNumber= random.randint(1,50)
    elif level(dif) == 3:
        myNumber= random.randint(1,100)
    
correct_number_10 = random.randint(1,10)

correct_number_50 = random.randint(1,50)

correct_number_100 = random.randint(1,100)

maxguess = 0
difficulty = input ("which level wil you chooooseee ")


while int(difficulty) == 1:

        guess = input("pick a number from 1-10:")

        if maxguess > 3:

            os.system('cls')

            menu()

            print("should have figured it out by now TOO MANY GUESES")

            correct_number_10 = random.randint(1,10)

            correct_number_50 = random.randint(1,50)

            correct_number_100 = random.randint(1,100)

            quit()

        if int(guess) > correct_number_10:

            print("number is too big, try smaller")

            maxguess = maxguess + 1

        if int(guess) < correct_number_10:

            print("number is too small, try  bigger")

            maxguess = maxguess + 1

        if int(guess) == correct_number_10:

            answer = input("that is correct, would you like to play again [YA OR NAW]  ")

            if answer == "YA":

                os.system('cls')

                menu()

                correct_number_10 = random.randint(1,10)

                correct_number_50 = random.randint(1,50)

                correct_number_100 = random.randint(1,100)

            if answer == "NAW":

                quit()


maxguess = 0

while int(difficulty) == 2:

        guess = input("pick a number from 1 to 50: ")

        if maxguess > 3:

            os.system('cls')

            menu()

            print("should have figured it out by now TOO MANY GUESES")

            correct_number_50 = random.randint(1,10)

            correct_number_50 = random.randint(1,50)

            correct_number_50 = random.randint(1,100)

            quit()

        if int(guess) > correct_number_50:

            print( "number is too big, try smaller ")

            maxguess = maxguess + 1

        if int(guess) < correct_number_50:

            print("number is too small, try  bigger ")

            maxguess = maxguess + 1

        if int(guess) == correct_number_50:

            answer = input("that is correct, would you like to play again [YA OR NAW] ")

            if answer == "YA":

                os.system('cls')

                menu()

                correct_number_10 = random.randint(1,10)

                correct_number_50 = random.randint(1,50)

                correct_number_100 = random.randint(1,100)

            if answer == "NAW":

                quit()
            
maxguess = 0

while int(difficulty) == 3:

        guess = input("pick a number form 1 to 100: ")

        if maxguess > 3:

            os.system('cls')

            menu()

            print("should have figured it out by now TOO MANY GUESES")

            correct_number_10 = random.randint(1,10)

            correct_number_50 = random.randint(1,50)

            correct_number_100 = random.randint(1,100)

            quit()

        if int(guess) > correct_number_100:

            print("number is too big, try smaller")

            maxguess = maxguess + 1

        if int(guess) < correct_number_100:

            print("number is too small, try  bigger")

            maxguess = maxguess + 1

        if int(guess) == correct_number_100:

            answer = input("that is correct, would you like to play again [YA OR NAW]")

            if answer == "YA":

                os.system('cls')

                menu()

                correct_number_10 = random.randint(1,10)

                correct_number_50 = random.randint(1,50)

                correct_number_100 = random.randint(1,100)

            if answer == "NAW":

                quit()