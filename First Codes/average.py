import os
#Tal Rogozinski
#Jan 14, 2022
#Declare variables, print variables, print types of data, learn some operators
#This symbol is for comments meaning the computer will ignore
# I want to clear my terminal
os.system('cls')
#Program is average of 3 tests
#Declare and Assign values
test1=89
test2=78.5
test3=86
Flag=False

#to display things on the screen we use the function print()
# print(type(test1),  type(test2), type(Flag))
Sum = test1 + test2 + test3
#Average we will divide
Average= Sum/3
print(Average)

#I want to print    The average of 3 tests is " number here"
print("The average of 3 tests is", Average)
print("Test1=", test1, end=" ")
print("Test2=", test2)

