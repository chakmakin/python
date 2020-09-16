"""
use of flush function()
"""
fout= open('flushlog.log','w+')
fout.write('This output is\n')
fout.write('My work status is\n')
fout.write('Working in JNV Bokaro\n')
fout.flush()
fout.write('OK\n')
fout.write('I am writing after using flush function()\n')
fout.write('This is final line to wrire\n')
fout.flush()
fout.close()