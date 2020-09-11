import functionCall
lst=[1,2,3,4,5,6,7,8,9,10]

def getMVal():
    return 4,5,6

if __name__=='__main__':
    print("Value after submission - ",functionCall.sumAction(lst))
    a,b,c = getMVal()
    print(a,b,c)
    print(getMVal())





