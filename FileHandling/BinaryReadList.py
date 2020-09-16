"""
Binary read code to file
"""
fout = open('binarylist.bin', 'rb')
lst = list(fout.read())
print(lst)
fout.close()
print('done')