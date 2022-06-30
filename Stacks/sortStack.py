from collections import deque
from pickletools import stackslice
def sorting(stack, top = 0):
    if len(stack) == 0:
        return stack
    num = stack.pop()
    stack = sorting(stack, num)
    stack = sortStack(stack, num)
    return stack
def sortStack(stack,k):
    if len(stack) == 0:
        stack.append(k)
        return stack
    else:
        top = stack.pop()
        if  top <= k:
            stack.append(top)
            stack.append(k)
            return stack
        else:
            stack = sortStack(stack, k)
            stack.append(top)
            return stack
stack = deque()
stack.append(-1)
stack.append(0)
stack.append(-2)
stack.append(1)
sorting(stack)
print(stack)