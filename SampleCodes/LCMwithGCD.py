#lcm.py
import math
arr = [2,7,3,9,4]
ans=arr[0]
i=1
while i<=len(arr)-1 :
    a2 = int(arr[i])
    ans = (ans*a2)/math.gcd(int(ans),a2)
    i=i+1

LCM = ans
print(LCM)
