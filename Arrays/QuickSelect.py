# The main idea for using this algorithm is to move all the largest elements towards the end of the list. 
# Once you have the required number of elements i.e k elements from the last, 
# you can return n-k index.
def quickSelect(arr, low, high, k):
    flag = True
    if low > high:
        return -1
    pivot = high
    i = low - 1
    for j in range(low, high):
        if arr[j] <= arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        else:
            continue
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    newPivot = i + 1
    
    if newPivot == len(arr)-1-k:
        return(arr[newPivot])
    #quicksort the left half 
    p = -1
    p = quickSelect(arr, low, newPivot-1, k)
    if p != -1:
        return p
    #quicksort the right half
    p = quickSelect(arr, newPivot+1, high, k)
    return p