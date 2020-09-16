"""
Use of pickle module to serialize (dump()) and
de-serialize (load()) the python object.
"""
import pickle

def pickleData() :
    fout = open('friendphone.bin','ab')
    phone1 = {'XYZ':9898445533,'Anand':6655443355,'Neeraj':5644456888}
    phone2 = {'ABC':9898445533,'Anand':6655443355,'Neeraj':5644456888}
    pickle.dump(phone1,fout)
    pickle.dump(phone2,fout)
    fout.close()
    print('OK I am done')

def unPickleData() :
    fout = open('friendphone.bin', 'rb')
    for i in range(4):
        phoneDict = pickle.load(fout)
        print(phoneDict)
    fout.close()
    print('OK I am done')

#To read file from disk
unPickleData()

#To write objet to file
# pickleData()