"""
Write 5 students name and phone using write lines.
"""
fout = open('student.dat', 'w')
# lst = []
# for i in range(5):
#     name = input('Enter name - ')
#     phone = input('Phone - ')
#     strData = 'Name - '+name+' Phone - '+phone+'\n'
#     lst.append(strData)
#
# print('List data is - ')
# print(lst)
# fout.writelines(lst)

for i in range(5):
    name = input('Enter name - ')
    phone = input('Phone - ')
    strData = 'Name - '+name+' Phone - '+phone+'\n'
    print(strData)
    fout.write(strData)
print("OK I am done")