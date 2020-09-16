"""
Read csv file using csv reader in form of dictionary.
"""
import csv

fout = open('stumarks.csv', 'r')
csv_reader = csv.DictReader(fout)  # reading file object
line_count = 0
for row in csv_reader:
    print(row['RollNo']+' -- '+row['Name']+' -- '+row['Subject']+' -- '+row['Marks'])

fout.close()
