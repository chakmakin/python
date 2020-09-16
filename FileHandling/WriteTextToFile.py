"""
Program to write data to file.
"""

fout = open("profile.txt", 'w')
str = "Class  - X Science\n"
str += "School - JNV Bokaro\n"
#str += "Address - Tanughat"
print(str)

fout.write(str)
fout.close()
