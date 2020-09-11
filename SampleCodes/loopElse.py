#program to get prime number from given range.

for n in range(112,210):
    for x in range(2,n) :
        if n%x==0:
            print (n,' equals', x,' * ',n//x)
            break
    else:
        print(n, ' is a prime number')
        
