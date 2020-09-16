'''
Created on Jul 3, 2020
Write a program to sort a dictionary's values using Bubble sort and
produce the sorted values as a line.
@author: admin
'''


def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1) :
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]       
    return lst


dic = {5:66, 6:44, 7:22, 3:54, 4:23, 2:54, 1:12}
l1 = list(dic.values())
print("list before sorting - ", l1)
l1 = bubbleSort(l1)
print("list after sorting - ", l1)
