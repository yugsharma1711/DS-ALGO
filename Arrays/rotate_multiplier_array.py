def rotateMultiplier(arr):
    k = 0
    actual_sum = sum(arr)
    round_sum = 0
    for i in range(len(arr)):
        round_sum += arr[i]*i
    s = len(arr)-1
    max_sum = round_sum
    while k < len(arr):
        round_sum += arr[k]*s - actual_sum + arr[k]
        if max_sum < round_sum:
            max_sum = round_sum
        k+=1
    
    return max_sum

arr = [8,3,1,2]
print(rotateMultiplier(arr))
    