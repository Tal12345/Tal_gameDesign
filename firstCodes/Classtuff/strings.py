#Tal Rogozinski
#1/31/2022 
#Objective = learn strungs and array of character
#Has many functions


import os, random
os.system('cls')
def menu():
    print("-----------------------------------------------------------------------------------------")
    print("----------------------------Welcome to the Word Game!------------------------------------")
    print("-----------------------------------Categories--------------------------------------------")
    print("--------------------1) Fruits----2) Animals---3) Computer parts--------------------------")
    print("----------------------What will your choice be????????????????---------------------------")
    print("-----------------------------------------------------------------------------------------")
MyName = "Tal Rogozinski"
myStatement="""" My name is the nicest name and the coolest one,
in the world

LOL"""

for elem in MyName:
    print(elem, end=" ")
guess=random.choice(MyName)
print(guess)
words=["Radio", "Clues", "robot", "peter", "suite"  ]
word=random.choice(words)
print(word)
check=True    
while check:
    letter=input("Dear user please give us a letter: ")
    if len(letter)>1 or not letter.isalpha():
        print("Bruh CHOOSE A LETTER")
    else: check=False
print("ready to play the game")
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end= " ")
    else:
        print("_", end=" ")

# print ("My last name begins with a " +MyName[4])
# print(myStatement)
# if 'LOL' in myStatement:
#     print('true')
# print('expert' not in myStatement)
# # a find() will return the index of the character you are looking for(first instance)
# INDEX= MyName.find("a")
# print(INDEX)
# #for loop is how many times who want to do something
# #finding th lenghth of your work
# wordLen =len(MyName)
# print(wordLen) #your last index is len -1 ( cuz it starts with zero )
# print(MyName[13])# when trying to find a specific letter in your name use []
# #for loop in range zero to limit
# for i in range (wordLen-1):
#     if "o" in MyName[i]:
#         print(i, end=", ")
# print("")
# print("done")
# myStatement=myStatement.upper()
# print(myStatement)
# # letter=input("Dear user please give us a letter: ")
# # print("Thank you, the letter is "+ letter)
# # if letter in myStatement:
# #     print("GREAT")

# check=True    
# while check:
#     letter=input("Dear user please give us a letter: ")
#     if len(letter)>1 or not letter.isalpha():
#         print("Bruh CHOOSE A LETTER")
#     else: check=False
# print("ready to play the game")
