"""
Read poem.txt file.
reading the file line by line.
"""

# print(open('poem.txt','r').read())
#fout = open(r"C:\Users\admin\Documents\PyCharmPrograms\BasicPython\XIIth202021\FileHandling\poem.txt",'r')
fout = open("poem.txt",'r')

str = ' '
while str :
    str = fout.readline()
    print(str, end='')

fout.close()