"""
Module to read text file from python.
@Author : XII Sc students
@Date : 25/07/2020
"""

#fout = open("address.txt",'r') #r - read mode
#fout = open("C:\\Users\\admin\\Documents\\PyCharmPrograms\\BasicPython\\XIIth202021\\FileHandling\\address.txt",'r') #r - read
#fout = open("C:\\Users\\admin\\Documents\\PyCharmPrograms\\BasicPython\\XIIth202021\\FileHandling\\address.txt",'r') #r - read
fout = open(r"C:\Users\admin\Documents\PyCharmPrograms\BasicPython\XIIth202021\FileHandling\address.txt",'r') #r - read
data = fout.read()
print(data)
fout.close()   #closing the file and send writtend data to hard disk.
