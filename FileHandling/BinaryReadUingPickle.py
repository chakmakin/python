"""
REad using pickle
"""
import pickle
fout = open('stulist.bin','rb')
lst=pickle.load(fout)
for i in lst :
    print(i)
fout.close()