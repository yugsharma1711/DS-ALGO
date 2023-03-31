from collections import deque
def nonRepeatingLongest(str):
    mapping = dict()
    max_counter = 0
    counter = 0
    q = deque()
    for i in str:
        if i in mapping:
            max_counter = max(max_counter, counter)
            if q[0] != i:
                temp = q.popleft()
                mapping.pop(temp)
                counter -= 1
            if q[0] == i:
                temp = q.popleft()
                mapping.pop(temp)
                counter -= 1
            mapping[i] = 1
            counter+= 1
            q.append(i)
        else:
            counter += 1
            mapping[i] = 1
            q.append(i)
    max_counter = max(max_counter, counter)
    return max_counter

str = 'aabaab!bb    '
print(nonRepeatingLongest(str))