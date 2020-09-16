"""
Read all lines using readlines() in the form of List
"""
fout = open('poem.txt', 'r')
lst = fout.readlines()
print(lst)
print(len(lst))