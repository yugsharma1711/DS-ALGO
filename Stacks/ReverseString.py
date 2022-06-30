from  collections import deque
str = 'DAKSHAYANI'
stack = deque()
for i in str:
    stack.append(i)
while len(stack) !=0:
    print(stack.pop(), end = '')
