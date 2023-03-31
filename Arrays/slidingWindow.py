from collections import deque
def slidingWindow(arr):
    q = deque()
    counter = 0
    sum = 0
    max_sum = 0
    for i in range(0, 3):
        sum += arr[i]
        q.append(arr[i])
    max_sum = sum
    for i in range(3, len(arr)):
        sum = sum - q.popleft() + arr[i]
        q.append(arr[i])
        if sum > max_sum:
            max_sum = sum
    return max_sum

arr = [1,2,3,4,5,6]
print(slidingWindow(arr))