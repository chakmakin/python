'''
Created on Jul 4, 2020

@author: admin
'''


def calcSum(x, y):  #x and y are parameter or formal parameter.
    s = x + y
    return s


num1 = float(input('Enter first number - '))
num2 = float(input('Enter second number - '))
sum = calcSum(num2, num1) #arument or actual parameter
print('sum of ', num1, ' and ', num2, ' is - ', sum)
print('sum of %f and %f is - %f ' % (num1, num2, sum))
