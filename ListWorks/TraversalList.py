'''
Created on Jun 25, 2020

@author: admin
'''
import math
lst = [56,44,33,54,23,12,65]

for i in lst :
    print(math.sqrt(i), end=' ')

print()    
for i in range(len(lst)):    
    print(math.sqrt(lst[i]), end=' ')