"""
Read csv file created using CSV Library
"""
import csv

fout = open('stumarks.csv', 'r')
csv_reader = csv.reader(fout, delimiter=',')  # reading file object
line_count = 0
for row in csv_reader:
    print(row)
fout.close()
