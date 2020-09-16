"""
Read and write/append using function.
"""


def readFromFile():
    fout = open("marks.dat", 'r')
    strData = fout.read()
    print(strData)
    fout.close()


def writeToFile():
    fout = open("marks.dat", 'w')
    stucount = int(input("Enter number of students in class - "))
    for i in range(stucount):
        writeForAll(fout)
    print('OK done')
    fout.close()


def appendToFile():
    fout = open("marks.dat", 'a')
    writeForAll(fout)
    print('OK done')
    fout.close()


def writeForAll(fout):
    roll = input("Enter roll no - ")
    name = input("Enter name - ")
    marks = input("Enter marks - ")
    rec = roll + ',' + name + ',' + marks + '\n'
    fout.write(rec)


while True:
    choice = input('Enter your choice[r/w/a/s] for read/write/append/SKIP - ')
    if choice == 'r':
        readFromFile()
    elif choice == 'w':
        dcheck = input("Do you realy want to write[y/n], It will delete all data -")
        if dcheck == 'y':
            writeToFile()
        else:
            print('Your data is still safe.!')
    elif choice == 'a':
        appendToFile()
    else:
        break
