m1 = int(raw_input("Enter number of rows of matrix 1: "))
n1 = int(raw_input("Enter number of columns of matrix 1: "))

mat1 = [[0 for j in range(n1)] for i in range(m1)]
mat2 = [[0 for j in range(m1)] for i in range(n1)]

print "Input matrix 1 below : "
for i in range(m1) :
    for j in range(n1) :
        mat1[i][j]=int(raw_input(str(i)+", "+str(j)+" : "))

print "Matrix entered is : "
for i in range(m1) :
    for j in range(n1) :
        print mat1[i][j],
    print
