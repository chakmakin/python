'''
Created on Jul 1, 2020
Insertion sort
@author: admin
'''
lst = [85, 12, 59, 45, 72, 51]
print('Original list - ', lst)

for i in range(1, len(lst)) :
    key = lst[i]
    j = i - 1
    while j >= 0  and key < lst[j] :
        lst[j + 1] = lst[j]  # shifting of heavy element to next node.
        j = j - 1
    else :
        lst[j + 1] = key
        print('Sorted list after %d is %s - '%(i, lst))

print('Sorted list - ', lst)
