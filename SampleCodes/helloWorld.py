'''
a = int(input("Enter firnst number - "))
b = int(input("Enter second number - "))
print (a,b)
a,b = b,a
print (a,b)


a = int(input("Enter firnst number - "))
b = int(input("Enter second number - "))
        
for i in range(a, b+1):
    print (i, "'s table - ")
    for j in range(1,11):
        print (i*j," ",end="")
    print()

print ('Product of {0} X {1}'.format(2,3)," = ",2*3)   
'''
x = int(input("Enter no of rows - "))
for i in range(x) :
    str ="*"
    for j in range(i):
        str+='*'
    print(str)

