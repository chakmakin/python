'''
Created on Aug 25, 2020
Linear Search Algorithm
@author: Admin
'''


def lSearch(arr, item):
    ind = 0
    while ind < len(arr) and item != arr[ind] :
        ind += 1
    if ind < len(arr) :
        return ind
    else :
        False


arr = [34, 33, 34, 12, 31, 11, 21]
item = 11
index = lSearch(arr, item)
print("Item found at index - ", index)
