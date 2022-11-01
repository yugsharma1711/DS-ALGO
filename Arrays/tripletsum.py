from operator import truediv

def checktripletSum(arr, sum):
    arr.sort()
    for i in range(len(arr)):
        required_value = sum - arr[i]
        low = i + 1
        high = len(arr) -1
        while low < high:
            if arr[low] + arr[high] == required_value:
                return True
            if arr[low] + arr[high] < required_value:
                low += 1
            if arr[low] + arr[high] > required_value:
                high -=1
    return False
            