'''
Created on Jul 2, 2020
Write a short Python code segment that prints the 
longest word in the list of words
@author: admin
'''

lst = ['akash', 'anand', 'joshna', 'ravi ranjan kumar gupta']
longest = ind = 0
for a in lst:
    length = len(a)
    if longest < length :
        longest  = length
        ind = lst.index(a)
     
print(ind, longest)
print('%s is longest word of length %s '%(lst[ind],longest))