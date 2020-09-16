'''
Created on Jul 6, 2020

@author: admin
'''


def sumOfNum(a, b, c):
    s = a + b + c
    return s


sum = sumOfNum(34, 23, 12)  # assigned the return value to sum
print(sum)

print(sumOfNum(21, 65, 34))  # return value is printed here

if sumOfNum(21, 2, 45) > 50 :
    print('value is greater then 50')
else :
    print('value is smaller then 50')