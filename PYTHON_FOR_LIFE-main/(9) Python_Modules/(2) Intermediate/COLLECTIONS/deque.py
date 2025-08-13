# DEQUE

from collections import deque

num = deque()

num.append(1)
num.appendleft(2)
num.append(4)

print(num)

num.popleft()
print(num)

num.clear()
print(num)

num.extendleft([3, 5, 6])
print(num)

num.rotate(1)
print(num)