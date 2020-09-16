'''
Created on Jun 29, 2020
write a program to create a dictionary containing names of 
competition winner students as key and number of their wins 
as value.
@author: admin
'''

num = int(input("Enter number of students - "))
compWin = {}

for i in range(num) :
    stuname = input("Enter name of student - ")
    gname = input("Enter name of game - ")
    wins = int(input("Enter no of wins - "))
    compWin[stuname+'-'+gname]=wins

print("Dictionary now is - ")
print(compWin)