"""
Reading the file line by line or one go.
"""

fout = open("poem.txt",'r')

str = ' '
size = 0
tsize = 0
while str :
    str = fout.readline()
    tsize += len(str)
    size += len(str.strip())
fout.close()
print("Size of file before removing spaces - ",tsize)
print("Size of file after removing spaces - ",size)