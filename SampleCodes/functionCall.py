def sumAction(lst):
    sum = 0
    for i in lst:
        sum+=i
    return sum

def userInput():
    lst = []
    for i in range(10):
        lst.append(int(input("Enter number - ")))
    return sumAction(lst)

if __name__=='__main__':
    print("Value after submission - ",userInput())
