# Tal Rogozinski
# January 19 2022

#Objective of today: Other opperators +-*/ ** exponent  % moduls format priniting
#             Format Printing escape character

#Program creating an equation
# and formatting the output
import os
os.system("cls")
#Declare varibale:
var1=10
var2=2
var3=2.9
var4=5

#Calculate equation given 
# print(2**4)

#Print Format
result= (3*var1 - 2*(var2)**2/var3)/var4
print("var1= %5d"% var1)
print("var2= %5d"% var2)
print("var3= %8.2f"% var3)
print("var4= %5d"% var4)
print("Result= %6.2f"% result, end=" -----")

print("\n The \" quotes\" tabs \t backslash \\")

