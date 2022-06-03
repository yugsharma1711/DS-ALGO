def quick_sort(arr, i, j):
    i_cpy = i
    j_cpy = j
    if i >= j:
        return
    pivot = i
    lesser_elements = 0
    for k in range(i, j+1):
        if arr[k] < arr[pivot]:
            lesser_elements += 1
    # making pivot to its appropriate position
    new_pivot  = pivot + lesser_elements
    temp = arr[pivot]
    arr[pivot] = arr[pivot + lesser_elements]
    arr[pivot + lesser_elements] = temp
    # checking right elements are lesser than pivot and greater elements are left side of pivot otherwise swapping
    while i <= j and i < new_pivot and j > new_pivot:
        if arr[i] < arr[new_pivot]:
            i += 1
        if arr[j] >= arr[new_pivot]:
            j -= 1
        if arr[i] >= arr[new_pivot] and arr[j] < arr[new_pivot]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j -= 1
            i += 1
    quick_sort(arr, i_cpy, new_pivot-1)
    quick_sort(arr, new_pivot+1, j_cpy)
lst = [6,6,5]
quick_sort(lst, 0, len(lst)-1)
print(lst)
