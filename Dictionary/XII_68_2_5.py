'''
Created on Jul 1, 2020
Write a program that finds an elements index/position
in a tuple WITHOUT using index()
@author: admin
'''

tpl = ('a', 'p', 'p', 'l', 'e')
chr = input('Enter a single letter without quotes - ')

#ind = tpl.index(chr)
#print('%s is at index position %s in %s'%(chr,ind,tpl))

if chr in tpl:
    count = 0
    for a in tpl :
        if a != chr :
            count += 1
        else :
            break
    #print("%s is at index %d in %s - " % (chr, count, tpl))
    print(chr," is at index ",count," in -",tpl)
else :
    print("%s is NOT part of tuple %s - " % (chr, tpl))
