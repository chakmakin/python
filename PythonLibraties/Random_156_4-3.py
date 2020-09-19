"""
In a school fest, three randomly students out of 100 students (Having roll
1-100) have to present bouquets to the guest. Help the school authorities
 choose three students randomly.
"""
import random


def getThreeRandomStudent():
    stu1 = random.randint(1, 6)
    stu2 = random.randint(1, 6)
    stu3 = random.randint(1, 6)
    return stu1, stu2, stu3

print("Three random students choose are -")
stu1, stu2, stu3 = getThreeRandomStudent()

if stu1 != stu2 and stu2 != stu3 and stu3 != stu1:
    print('1. - ', stu1)
    print('2. - ', stu2)
    print('3. - ', stu3)
else:
    print("try again")
