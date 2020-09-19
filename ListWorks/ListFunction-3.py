'''
Created on Jun 26, 2020

@author: admin
'''
lst = [45,33,44,23,56,44]

print("List before reverse - ",lst)
lst.reverse()
print("List after reverse - ",lst)

print("List before sorting - ",lst)
#lst.sort()
print("List after sorting - ",lst)
lst.sort(reverse=True)
print("List after sorting - ",lst)