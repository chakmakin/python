"""
program to demonstrate the use of
standard input and standard output device of file
"""
import sys
fout = open('readkeyboard.txt','a+')
# line1 = fout.readline()
# line2 = fout.readline()
# print('Line print using print() function - ',line1)
# print('Line print using print() function - ',line2)
# sys.stdout.write('Line print using sys.stdout - '+line1)
# sys.stdout.write('Line print using sys.stdout - '+line2)
# sys.stdout.write('Reading from file is done')

# name = input("Enter your name - ")
# address = input("Enter your address - ")
name = sys.stdin.readline(5)
address = sys.stdin.readline(7)

rec = '\n'+name+','+address
fout.write(rec)
fout.close()