def quick_sort(arr, start, end):
    if start >= end :
        return 
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = start
    counter =  0
    for i in arr[start:end+1]:
        if i < arr[pivot]:
            counter += 1
    arr[pivot], arr[start + counter] = arr[start + counter], arr[pivot]
    pivot = start + counter
    i = start
    j = end
    while i < pivot and j > pivot:
        if arr[i] > arr[pivot] and arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            continue
        if arr[i] <= arr[pivot]:
            i += 1
        if arr[j] > arr[pivot]:
            j -= 1
    return pivot
arr = [2,1,23]
quick_sort(arr, 0,2)
print(arr)