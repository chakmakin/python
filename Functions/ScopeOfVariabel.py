'''
Created on Jul 8, 2020

@author: admin
'''


def state1():
    global tigers
    tigers = 15
    print('line - 11 Tiget from function - ',tigers)


tigers = 95
print('line - 15 Tiget before function - ',tigers)
state1()
print('line - 17 Tiget after function - ',tigers)