'''
Created on Jul 2, 2020
Write a program that checks for presence of a value 
inside a dictionary and prints its key
@author: admin
'''

info = {'Riya':'cs', 'Mark':'eco', 'Ishpreet':'eng', 'Kamaal':'evs'}
inp = input("Enter the subject to search - ")
if inp in info.values() :
    for a in info :
        if info[a] == inp :
            print('%s studies %s' % (a, inp))
            break
else :
    print('Given subject %s is not studied by any one' % (inp))    
