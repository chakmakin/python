'''
Created on Sep 10, 2020
Backward loop python in List
@author: admin
'''

lst = [1, 2, 11, 9, 19]
top = len(lst) - 1
print(lst[top], '<-- top')
for a in range(top - 1, -1, -1):
    print(lst[a])
