'''
Created on Jul 4, 2020

@author: admin
'''

print(__name__)

def sumof3Multiplies1(n):
    s = n * 1 + n * 2 + n * 3
    return s


def sumof3Multiplies2(n):
    s = n * 1 + n * 2 + n * 3
    print(s)
    print(__name__)

sumof3Multiplies2(3)
sumof3Multiplies2(13)

'''
sum = sumof3Multiplies1(2)
print(sum)

s1 = sumof3Multiplies2(3)
print(s1)
print(sumof3Multiplies2(3))

'''