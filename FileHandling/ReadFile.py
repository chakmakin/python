"""
Read data from file
"""
fout = open('profile.txt', 'r')
str = fout.read(20)
print(str)
print(type(str))
print("=========")
str = fout.read(15)
print(str)
print("=========")
str = fout.read()
print(str)
print("=========")
str = fout.read()
print('Reading from last - ',str)
print("=========")
fout.close()
