"""
Binary Write code to file
"""
fout = open('textlist.txt', 'wb')
list = [9,1,2,5,9,10]
arr=bytearray(list)
fout.write(arr)
fout.close()
print('done')