def merge_sort(arr, i, j):
    if i == j:
        return
    else:
        mid = i + j
        mid = mid // 2
        merge_sort(arr, i , mid)
        merge_sort(arr, mid+1, j)
        merge(arr, i, mid, j)


def merge(arr, i, mid, j):
    k = mid + 1
    i_cpy = i
    sortedarr = []
    while i < mid+1 and k <= j:
        if arr[i] <= arr[k]:
            sortedarr.append(arr[i])
            i += 1
        else:
            sortedarr.append(arr[k])
            k += 1
    while i < mid+1:
        sortedarr.append(arr[i])
        i += 1
    while k <= j:
        sortedarr.append(arr[k])
        k += 1
    i = i_cpy
    for lst in sortedarr:
        arr[i] = lst
        i += 1
        if i > j:
            return


sample = [5, 1, -1, 0,3,4,2]
merge_sort(sample, 0, len(sample)-1)
print(sample)