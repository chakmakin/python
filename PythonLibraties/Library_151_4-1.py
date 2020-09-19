"""
Program that reads a number, then converts it into octal and
hexadecimal equivalent number using built-in function.
"""
intnum = int(input("Enter any number to convert into OCT and HEX - "))
onum = oct(intnum)
xnum = hex(intnum)
bnum = bin(intnum)
print("Octal of ", intnum, ' is - ', onum)
print("Hexadecimal of %d is - %s" % (intnum, xnum))
print("Binary of %d is - %s" % (intnum, bnum))
