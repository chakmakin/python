"""
Program that input a real number and converts it to nearest integer uing
two different built-in function. It also display the given number rounded
off to 3 place after decimal.
"""

rnum = float(input("Enter any real number - "))
inum = int(rnum)
round1 = round(rnum)
print("Integer of ", rnum, ' is - ', inum)
print("Rounded value of ", rnum, ' is - ', round1)
roundat3 = round(rnum, 3)
print("Three place Rounded value of ", rnum, ' is - ', roundat3)
