import random
"""
print(random.random())
print(random.random())
print(random.random())
print(random.random())
"""

"""
#random.random()*(upper-lower)+lower
for i in range(5) :
    random1 = random.random()*(4-2)+2
    print(random1)
"""


for i in range(1,4) :
    random1 = random.randint(1,6)
    if random1 == 6:
        print(i,'Chance -',random1, '(Wow...)')
    else :
        print(i,'Chance -',random1)
