
def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
def merge(arr, low, mid, high):
    i = low
    k = mid + 1
    j = high
    sortedarr  = []
    while i <= mid and k <= high:
        if arr[i] <= arr[k]:
            sortedarr.append(arr[i])
            i += 1
        else:
            sortedarr.append(arr[k])
            k += 1
    while i <= mid:
        sortedarr.append(arr[i])
        i += 1
    while k <= high:
        sortedarr.append(arr[k])
        k += 1
    i = low 
    for value in sortedarr:
        arr[i] = value
        i += 1

arr=  [2,4,5,1,4, -1, 0 , 3]
merge_sort(arr, 0, len(arr)-1)
print(arr)