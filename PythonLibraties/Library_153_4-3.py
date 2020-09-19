"""
program that inputs a main string and then creates encrypted string by
embedding a sort symbol based string after each character. The program should
able to produce the decrypted string from encrypted string.
"""
def encrypt(str, enkey) :
    return enkey.join(str)

def decrypt(str, enkey) :
    return str.split(enkey)

mainStr = input('Enter String to be encrypted- ')
encrCode = input('Enter Code to encrypt- ')
encrpytStr = encrypt(mainStr, encrCode)
print("Encrypted String is - ",encrpytStr)
lstDecrupt = decrypt(encrpytStr,encrCode)
print("Decrypted List is - ",lstDecrupt)
deStr = ''.join(lstDecrupt)
print("Decrypted String is - ",deStr)
