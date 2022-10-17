def mostRightBS(arr, low, high, curr_index = -1):
    if low > high:
        return curr_index
    mid = low + high
    mid = mid // 2
    if arr[mid] == 1:
        return mostRightBS(arr, mid+1, high, mid)
    else:
        return mostRightBS(arr, mid+1, high, curr_index)
def max1s(arr):
    mostRight = -1 
    mostRight_index = -1
    for i in range(len(arr)):
        _index = mostRightBS(arr[i], 0, len(arr[1]))
        if _index > mostRight:
            mostRight = _index
            mostRight_index =i
    return mostRight_index