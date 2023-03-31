from collections import deque
def subArrayWithKDifferent(arr,k):
    mapping = dict()
    q = deque()
    counter = 0
    good_array = 0
    for i in arr:
        if i in mapping:
            mapping[i] += 1
            q.append(i)
        else:
            mapping[i] = 1
            counter += 1
            q.append(i)
            if counter == k:
                print(q)
                first_element = q.popleft()
                counter = 0
                mapping.pop(first_element)
                good_array += 1
    return good_array

arr = [1,1,1,3]
print(subArrayWithKDifferent(arr, 3))                
            
            