'''
Created on Aug 25, 2020
Insertion in array using bisect module
@author: Admin
'''

import bisect
ar = [2, 4, 5, 15, 17, 19, 23, 25]
print("Array before insort is  - ", ar)
item = int(input("Enter the element to be inserted - "))
index = bisect.bisect(ar, item)  # will return the index where insertion work
bisect.insort(ar, item)  # will insert the item
print("Array after insort is  - ", ar)
print("Item inserted at index - ", index)
