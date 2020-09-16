"""
Program to display the size of a file in bytes.
"""

fout = open('profile.txt','r')
str = fout.read()
lenstr = len(str)
print('Size of file is - ',lenstr)