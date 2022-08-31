from collections import deque

def revStack(s):
    length = len(s)
    for i in range(length//2):
        topElement=s.pop()
        s=insertAtBottom(s,topElement)
    return s
def insertAtBottom(s, ele, topElement=-1):
    if len(s) == 0:
        s.append(ele)
        return s
    topElement = s.pop()
    s = insertAtBottom(s, ele, topElement)
    s.append(topElement)
    return s
s = deque()
str = 'YUG'
for i in str:
    s.append(i)
s= revStack(s)
while len(s)!=0:
    print(s.pop())