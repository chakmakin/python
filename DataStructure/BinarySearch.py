'''
Created on Aug 25, 2020
Binary Search Algorithm
@author: Admin
'''


def bsearch(arr, item):
    beg = 0
    last = len(arr) - 1
    iteration = 1
    while beg <= last:
        print("Iteration count - ", iteration)
        iteration += 1
        mid = (beg + last) // 2
        if item == arr[mid]:
            return mid
        elif (item > arr[mid]):
            beg = mid + 1
        else:
            last = mid - 1
    else:
        return False


# main
ar = [2, 4, 5, 15, 17, 19, 23, 25]
item = 19
index = bsearch(ar, item)
if index:
    # print('Item found at index ', index)
    print('Item %d found at index - %d' % (item, index))
else:
    print("sorry no match found")
