'''
Created on Jul 1, 2020
Bubble sort program
@author: admin
'''

lst = [5, 1, 4, 2, 8]
print('Original list - ', lst)
n = len(lst)

pas= 1
for i in range(n):
    for j in range(0, n - i - 1) :
        if lst[j] > lst[j + 1] :
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print('Sorted list after %d pass is %s - '%(pas, lst))    
    pas +=1        

print('Sorted list - ', lst)