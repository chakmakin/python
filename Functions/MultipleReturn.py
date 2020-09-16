'''
Created on Jul 7, 2020

@author: admin
'''
import math


def sqrtOfNum(a, b, c):
    a = math.sqrt(a) 
    b = math.sqrt(b) 
    c = math.sqrt(c) 
    return a, b, c


# storing multiple return in tuple
t = sqrtOfNum(1, 2, 3)
print(t)

# storing multiple return in tuple
a, b, c = sqrtOfNum(10, 20, 30)
print(a, b, c)
