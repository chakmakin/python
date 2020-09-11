'''Even Number Check '''
'''
def what1(n):
    if n<0:
        n=-n
    while n>0 :
        if n%2==1:
            return False
        n/=10
    return True

print(what1(5))
print(what1(-4))
print(what1(4))
print(what1(14))
print(what1(11))
print()

def what2(n):
    i=1
    while i*i<n :
        i+=1
    return i*i == n,i

print(what2(25))
print(what2(-4))
print(what2(4))
print(what2(14))
print(what2(11))
print()
'''
def what3(x,n):
    if n<0:
        n = -n
        x = 1/x
    z = 1
    while n>0:
        if n%2==1:
            z*=x
        x*=x
        n=n//2
    return z
print(what3(4,5))
print(what3(2,2))

