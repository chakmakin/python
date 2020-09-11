lst = [23,45,67,28,12]
for i in range(len(lst)):
    temp = lst[i]
    for j in range(i,len(lst)) :
        if lst[j]<temp:
            lst[j]=temp
            break
    print(lst)
print()
print(lst)
        
    
