'''
Print a Fibonacci series upto n.
'''

'''fin is for getting the febonacci of n'''
def fib(n) :
    
    a,b = 0,1
    while a<n :
        print (a,end=' ')
        a,b = b,a+b
    print()

fib(2000)
