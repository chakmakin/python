"""
Writing into CSV tile using csv writer
https://realpython.com/python-csv/
"""
import csv
fout = open('stumarks.csv', 'a')
csv_writer = csv.writer(fout, delimiter=',')
lstStudent1 = [12,"Udit VERMA","PHY",42]
csv_writer.writerow(lstStudent1)
fout.close()
print('OK')