import random
stack = random.sample(range(1,101),3)
print(stack)

from collections import deque
queue = deque([3,4,5,67,3])
print(queue.popleft())
print(queue)
queue.append(5)
print(queue)

squares = [x**2 for x in range(20)]
print(squares)

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
#result = [x for x in v if x%3==0]
#print (result)

v =[[1,2,3],[4,5,6],[7,8,9]]
res =  [num for ele in v for num in ele]
print(res)

v =[[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]]
ress = [num for ele1 in v for ele2 in ele1 for num in ele2]
print(ress)

from math import pi
r = 20
a = [round(2*r*pi) for i in range(1,6)]
print(a)
