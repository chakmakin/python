'''
Created on Jun 20, 2020

@author: admin
'''
num = int(input("Enter number to check prime - "))

i = 2
while i<num :
    if num%i==0 :
        print("%d is not a prime number" %(num))
        break
    i+=1
else :
    print("%d is a prime number" %(num))