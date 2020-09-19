'''
Created on Jun 20, 2020

@author: admin
'''
num = int(input("Enter number to check prime - "))

for i in range(2,num):
    if num%i==0 :
        print("%d is not a prime number" %(num))
        break
else :
    print("%d is a prime number" %(num))