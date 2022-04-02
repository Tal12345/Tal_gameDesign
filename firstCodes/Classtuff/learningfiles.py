#Tal Rogozinski
# Learning FIles:
#open/create a file b)write a fuile 'w'
#append 'a'
#reas'r'
# close()

#where do I wnat to put the file?

from unicodedata import name
import pygame as p, os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Jesse'
#how to print the dtae/time
# print(date.strftime('%d/%m/%Y'))
scoreLine=str(score)+"\t "+name+" \t"+ (date.strftime('%d/%m/%Y')+'\n') 
print(scoreLine)
#open a file nd write
myFile=open('firstCodes\Classtuff\cireate.txt','w')
myFile.write(scoreLine)

myFile.close()

score=345
name='Jay'
#how to print the dtae/time
# print(date.strftime('%d/%m/%Y'))
scoreLine=str(score)+"\t "+name+"\t "+ (date.strftime('%d/%m/%Y')+'\n') 
myFile=open('firstCodes\Classtuff\cireate.txt','a')
myFile.write(scoreLine)
myFile.close()
myFile=open('firstCodes\Classtuff\cireate.txt','r')
lines=myFile.readline()
print(lines)
lines=myFile.readline()
print(lines)
myFile.close()
