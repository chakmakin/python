"""
Write 5 students record to file.
"""
fout = open("student.dat", 'w')
for i in range(5):
    name = input("Enter name - ")
    fout.write(name + '\n')
    # fout.write('\n')
