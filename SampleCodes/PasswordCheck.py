num=(0,1,2,3,4,5,6,7,8,9)
lcase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spec =('$','#','@')

passwords=('AbCAA#123','123a','87992CCgg#@')
flag = True
for i in passwords:
    for j in i:
        if j in num or j in lcase or j in lcase.captilize() or j in spec :
            flag = True
        else:
            break
    print (passwords[i])

