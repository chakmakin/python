'''
Created on Jun 20, 2020
Write a program that multiplies two interger number without using
the * operator, using repeated adition.
@author: admin
'''
n1 = int(input("Enter first number - "))
n2 = int(input("Enter second number - "))
product = 0
count = n1
while count>0:
    count = count-1
    product = product+n2
    print(product)

print("The product of ",n1,' and ',n2," is ",product)