'''
Created on Sep 9, 2020
Stack implementation using List in Python
@author: Admin
'''


def isEmpty(stk):
    if len(stk) == 0:
        return True
    else :
        return False


def push(stk, item):
    stk.append(item)
    top = len(stk) - 1


def pop(stk):
    if isEmpty(stk) :
        return 'underflow'
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item


def peek(stk):
    if isEmpty(stk) :
        return 'underflow'
    else:
        top = len(stk) - 1
        return stk[top]


def display(stk):
    if isEmpty(stk) :
        return 'underflow'
    else:
        top = len(stk) - 1
        print(stk[top], ' <- top')
        for a in range(top - 1, -1, -1) :
            print(stk[a])


#==== Main ====
stack = []
top = None

while True :
    print('====================')
    print('Stack Operations')
    print('1. PUSH')
    print('2. POP')
    print('3. PEEK')
    print('4. DISPLAY STACK')
    print('5. EXIT')
    
    ch = int(input("Enter your choice from [1-5] : "))
    if ch == 1 :
        item = int(input('Enter item : - '))
        push(stack, item)
    elif ch == 2 :
        item = pop(stack)
        if item == 'underflow':
            print('UNDERFLOW ! Stack is empty')
        else :
            print('Popped item is - ', item)
    elif ch == 3 :
        item = peek(stack)
        if item == 'underflow':
            print('UNDERFLOW ! Stack is empty')
        else :
            print('TOPMOST item is - ', item)
    
    elif ch == 4:
        display(stack)
    elif ch == 5 :
        break
    else :
        print("Invalid choice ! Please try again !")
    
