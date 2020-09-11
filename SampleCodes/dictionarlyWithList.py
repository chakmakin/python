'''
program to add key value from user
'''
d = {}
for a in range(3):
    key = input("Enter key name - ")
    if a not in d.keys():
        vals = []
        for b in range(2):
            v = input("Enter value for - ")
            vals.append(v)
        #print (vals)
        d[key] = vals

print(d.items())
