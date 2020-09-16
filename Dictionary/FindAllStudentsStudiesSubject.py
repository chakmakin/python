'''
Created on Jul 2, 2020
Write a program that checks for presence of a value 
inside a dictionary and prints its key
---- Find all students studies any subjet ---
@author: admin
'''

info = {'Riya':'cs', 'Mark':'eco', 'Ishpreet':'eng', 'Kamaal':'evs', 'Udit':'cs', 'Joshna':'cs'}
inp = input("Enter the subject to search - ")
dic = {}
if inp in info.values() :
    for a in info :
        if info[a] == inp :
            dic[a] = inp  # adding new element in dic
    
    for a in dic :
        sub = dic[a]
        print('%s studies %s' % (a, sub))
        
else :
    print('Given subject %s is not studied by any one' % (inp))    
