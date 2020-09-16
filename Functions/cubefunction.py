'''
Created on Jul 3, 2020

@author: admin
'''


def cube(x):
    res = x ** 3
    return res

cval = cube(4)
print(cval)

num = 2
print(cube(num))

n1 = int(input("Enter number to calculate cube - "))
print(cube(n1))

dubleOfCube = 2* cube(n1)
print('Duble of cube is - ',dubleOfCube)