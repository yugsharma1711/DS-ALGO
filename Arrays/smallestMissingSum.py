def smallestMissingSum(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != 0 and arr[i+1] - arr[i] != 1:
            return arr[i] + 1
    return arr[-1] + 1

arr = [1,1,1]
print(smallestMissingSum(arr))  