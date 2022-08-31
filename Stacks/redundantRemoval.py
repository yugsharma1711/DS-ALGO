from collections import deque
def findRedundantBrackets(s:str):
    stack = deque()
    i = 0
    while i < len(s):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        if (s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/') and len(stack) != 0:
                    while i != len(s):
                        if s[i] == ')' or s[i] == '}' or s[i] == ']':
                            stack.pop()
                            break
                        i += 1
        i += 1                            
    if len(stack) == 0:
        return 'No'
    else:
        return 'Yes'

print(findRedundantBrackets('(a+b)'))