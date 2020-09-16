"""
Program to display the number of lines in the file.
"""
fout = open('profile.txt','r')
lststr = fout.readlines()
noofline = len(lststr)
print('Total no of lines are - ',noofline)