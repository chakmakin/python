'''
Created on Aug 25, 2020
Binary Search in descending order
@author: Admin
'''


def bSearchDesc(arr, item):
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
            last = mid - 1
        else:
            beg = mid + 1
    else:
        return False


# main
ar = [62, 54, 45, 45, 37, 29, 23, 15]
item = 45
index = bSearchDesc(ar, item)
if index:
    # print('Item found at index ', index)
    print('Item %d found at index - %d' % (item, index))
else:
    print("sorry no match found")
