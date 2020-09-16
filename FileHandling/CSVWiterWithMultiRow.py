"""
CSV Multirow writing.
"""
import csv
with open('phone.csv','w') as fout :
    phoneWriter = csv.writer(fout, delimiter=',')
    phoneWriter.writerow(['John Smith', 'Accounting', 'November'])
    phoneWriter.writerow(['Erica Meyers', 'IT', 'March'])

print('OK Done')
