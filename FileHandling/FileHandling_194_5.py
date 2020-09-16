"""
QNO -5. Wtite a function stats() that accept a filename and reports
the file's longest line.
"""

out = open('poem.txt', 'r')


def stats(fout):
    longline = ""
    poemlines = out.readlines()
    for line in poemlines:
        if len(line) > len(longline):
            longline = line
    print('Longes line is - ', longline)
    print('Length of line is - ', len(longline))


stats(out)
