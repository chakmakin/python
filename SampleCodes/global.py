y = 99
def testfun(x):
    global y
    print(y)
    y = y-5    
    print(y)
    print (x)

testfun(44)
print (y)
