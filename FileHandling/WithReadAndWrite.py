"""
Read and write using with block
"""

with open(r'..\functions\relativepath.txt','a') as fout :
    rec = 'Email - abc@abc.com'
    fout.write(rec)
print('OK done')
print(fout.read())