from collections import deque
def deleteMiddle(inputStack, N):
    outputStack = deque()
    counter = 0
    while counter != N:
        if counter == N // 2:
            counter += 1
            inputStack.pop()
            continue
        outputStack.append(inputStack.pop())
        counter += 1
    while len(outputStack) != 0:
        print(outputStack.pop(), end = ' ')
    print()

(deleteMiddle([1,2,3], 3))
deleteMiddle([1,2,3], 3)