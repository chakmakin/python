'''
Created on Sep 4, 2020
Program 9.5 from page 315 
@author: Admin
'''


def addLoc(cmp):
    dd = cmp[0:2]
    lnplaned = len(planned)
    if lnplaned == 0 :
        planned.append(cmp)
    else:
        last = planned[lnplaned - 1]
        if int(dd) >= int(last[0:2]):
            planned.append(cmp)
        else :
            for i in range(lnplaned) :
                cp = planned[i]
                if int(dd) >= int(cp[0:2]):
                    planned.insert(i, cmp)
                    break


def conductCamp(cmp):
    conducted.append(cmp)
    planned.remove(cmp)

    
def search(cmp, lst):
    ln = len(lst)
    for i in range(ln) :
        if cmp in lst[i] :
            return lst[i]
        else :
            return False


def report():
    lenp = len(planned)
    lenc = len(conducted)
    print('\t REPORT')
    print('------------')
    print('Camps conducted so far - ', lenc)
    print('People served in camps so far - ', ppl)
    print('Camps is to be conducted  - ', lenp)
    print('------------')


def display():
    print('\nCamps planned : ', end='')
    for i in planned :
        print(i, end=' , ')
    print('...!!')
    print('\nCamps to be conducted : ', end='')
    for i in conducted :
        print(i, end=' , ')
    print('...!!')


#main-----
planned = []
conducted = []
ppl = 0
ch = 0
while (ch != 6):
    print("\t")
    print("\tMENU")
    print("\t")
    print('1. ADD CAMP LOCATION')
    print('2. CAMP CONDUCTED')
    print('3. LOOK FOR CAMP')
    print('4. REPORT')
    print('5. DISPLAY LIST')
    print('6. EXIT')
    ch = int(input("Enter your choice between [1-6] -"))
    if ch == 1 :
        cm = input("Enter camp location - ")
        dd = input("Enter date of the month[only DD] - ")
        cmp = dd + cm
        addLoc(cmp)
    elif ch == 2 :
        cm = input("Camp conducted at location - ")
        p = int(input("How many people are served in this camp? - "))
        ppl = ppl + p
        result = search(cm, planned)
        if result == False :
            print("Sorry no such camp in the list")
        else :
            conductCamp(result)
    elif ch == 3 :
        cm = input("Enter camp location - ")
        r1 = search(cm, planned)  # result 1
        if r1 == False :
            r2 = search(cm, conducted)  # result 2
            if r2 == False:
                print(cm, " was conducted on date ", dd, " of this month")
            else :
                dd = r2[0:2]            
                print(cm, "was conducted on date", dd, "of this month")
        else :
            dd = r1[0:2]
            print(cm, "camp is to be conducted on date", dd, "of this month") 
    elif ch == 4 :
        report()
    elif ch == 5 :
        display()
    elif ch != 6:
        print("Wrong choice given! Enter choice between 1 to 6 only")
    else :
        print("***THANK YOU***")
