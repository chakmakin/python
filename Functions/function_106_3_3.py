'''
Created on Jul 8, 2020

@author: admin
'''


def arCal(x, y):
    return x + y, x - y, x * y, x / y, x % y


t = arCal(4*5, 5+7)
print(t)

a, b, c, d, e = arCal(4, 5)
print(a, b, c, d, e)
