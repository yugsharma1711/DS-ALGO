def closestSum(arr, x):
    low = 0
    high = len(arr)-1
    diff = x
    ans = []
    while low < high:
        sum = arr[low] + arr[high]
        curr_diff = abs(x - sum)
        if curr_diff == 0:
            return (arr[low], arr[high])
        elif sum > x:
            if curr_diff < diff:
                diff = curr_diff
                ans = [arr[low], arr[high]]
            high -= 1
        else:
            if curr_diff < diff:
                diff = curr_diff
                ans = [arr[low], arr[high]]
            low += 1
    return ans

arr = [10, 22, 28, 29, 30, 40]
closestSum(arr, 54)