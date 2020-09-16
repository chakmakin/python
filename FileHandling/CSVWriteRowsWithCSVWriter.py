"""
Writing muliple rows into CSV tile using csv writer
at one go using writerows() function.
https://realpython.com/python-csv/
"""
import csv
fout = open('stumarks.csv', 'a')
csv_writer = csv.writer(fout, delimiter=',')
lstStudent1 = [13,"Akash","PHY",42]
lstStudent2 = [14,"Laxmi","PHY",41]
lstStudent3 = [15,"Suresh","PHY",47]
lstStudent4 = [16,"Praful","PHY",44]
lstAll = []
lstAll.append(lstStudent1)
lstAll.append(lstStudent2)
lstAll.append(lstStudent3)
lstAll.append(lstStudent4)
print(lstAll)
csv_writer.writerows(lstAll)
fout.close()
print('OK')