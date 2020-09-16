"""
QN 5 - Write code to store name and phone number in CSV file.
"""
file = open('contacts.csv','a')
name = input('Enter your name - ')
contact = input('Enter your phone number - ')
file.write(name+','+contact+'\n')
file.close()
print('Done')