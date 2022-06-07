def permutation(arr, output_arr, powerset):
    if len(arr) == 0:
        powerset.append(output_arr)
        return
    else:
        for i in arr:
            arr_cpy = arr[:]
            output_arr_cpy = output_arr[:]
            output_arr_cpy.append(i)
            arr_cpy.remove(i)
            permutation(arr_cpy, output_arr_cpy, powerset)

arr = [1,2,3,5]
output = []
powerset = [[]]
permutation(arr, output, powerset)
print(powerset)