def merge(arr1, arr2):
    i = 0
    j = 0
    merged_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j+=1
    return merged_array
def median(arr1, arr2):
    merged_array = merge(arr1, arr2)
    length = len(merged_array) 
    if length % 2 == 0:
           return (merged_array[length//2] + merged_array[(length-1)//2]) / 2
    else:
        return merged_array[(length-1)//2]
arr1 = [1,2]
arr2 = [3,4]
print(median(arr1, arr2))