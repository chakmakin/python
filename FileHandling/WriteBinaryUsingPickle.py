"""
Writing using pickle
"""
import pickle
fout = open('stulist.bin','ab')
lstStudent1 = [12,"Udit VERMA","PHY",42]
lstStudent2 = [54,"Udit VERMA","PHY",42]
lstStudent3 = [76,"Udit VERMA","PHY",42]
pickle.dump(lstStudent1,fout)
pickle.dump(lstStudent2,fout)
pickle.dump(lstStudent3,fout)
fout.close()
print('oK')