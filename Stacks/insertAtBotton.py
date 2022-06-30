from collections import deque
def insertAtBottom(stack,x):
    if len(stack) == 0:
        stack.append(x)
        return stack
    else:
        k = stack.pop()
        stack = insertAtBottom(stack, x)
        stack.append(k)
stack = deque()
stack.append(1)
insertAtBottom(stack, 0)
print(stack)