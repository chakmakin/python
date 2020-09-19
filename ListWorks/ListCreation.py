'''
Created on Jun 24, 2020

@author: admin
'''
l1 = ['red','green','blue','yellow']

'''
l2 = l1
l1[0] = "orange"
print(l1)
print(l2)
'''
l2 = list(l1)
l1[0] = "orange"
print(l1)
print(l2)