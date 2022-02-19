# Tal Rogozinski
# 2/16/22
#lists
import os, random
os.system('cls')

Fruits=["mango", "bananas", "bananas", "watermelon", "papaya", "oranges", "strawberries", "apples", "blackberriew", "cantalope", "blueberries", "tangerine"]
#length of your array
size= len(Fruits)
print(size)
print(Fruits[-2])
Fruits.append("mango")
for i in range(size): #12 is not included
    print(Fruits[i])
print(Fruits[size-1])
print(Fruits[-2])
print(Fruits.count('bananas'))
list2=[3,6,8,9,10]
Fruits.append(list2)
print("append \n",Fruits)
Fruits.pop(-1)
Fruits.extend(list2)
print("extend \n",Fruits)
Fruits.insert(2,"papaya")
print(Fruits)
