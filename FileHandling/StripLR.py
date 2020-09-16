"""
Removing leading and trailing spaces from line
"""
fout = open('poem.txt','r')
line = fout.readline()
print('Length of line - ',len(line))
line = line.rstrip('\n')
print('Length of line afer rstrip - ',len(line))
line = line.lstrip()
print('Length of line afer lstrip - ',len(line))
line = line.strip()
print('Length of line afer strip - ',len(line))
