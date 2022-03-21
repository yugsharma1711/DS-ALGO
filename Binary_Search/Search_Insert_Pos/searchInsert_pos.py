def search_index(arr, start, end, key):
    if start >= end:
        if key > arr[start]:
            return start + 1
        else:
            return start
    mid = start + end
    mid = mid // 2
    if arr[mid] > key:
        return search_index(arr, start, mid-1, key)
    elif arr[mid] < key:
        return search_index(arr, mid + 1 , end, key)
    else:
        return mid

arr = [3,5,7,9,10]
print(search_index(arr, 0, len(arr)-1,8))