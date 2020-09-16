"""
Read the csv file and display name and contacts
"""
file = open('contacts.csv','r')
lstcontacts = file.readlines()
for line in lstcontacts :
    lstline = line.split(',')
    print('Name : ',lstline[0],'\t','Phone : ',lstline[1])
print('Done')
file.close()