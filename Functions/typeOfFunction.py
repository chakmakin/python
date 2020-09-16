'''
Created on Jul 3, 2020

@author: admin
'''
import math
import random
a = 10
print(type(a))  #built-in function

#sin() and randint() is function defined in module.
print('sin galue of ',a, 'is - ', math.sin(a))
print('random from first 1-6 number is -',random.randint(1,6))

#cube is user defined function
def cube(x):
    res = x ** 3
    return res

cval = cube(4)
print(cval)

name = input('Enter your name - ')
def sayHi(nm):
    print('Good morning ',nm)

sayHi(name)
sayHi('Anand')
