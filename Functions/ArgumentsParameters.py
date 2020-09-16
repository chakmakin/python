'''
Created on Jul 6, 2020

@author: admin
'''


def alterList (lst):
    for i in range(len(lst)) :
        lst[i]=lst[i]*2
        
l= [1,2,3,4,5]
print(l)
alterList(l)
print(l)