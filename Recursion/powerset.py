def power_set(arr, powerset, output, i):
    if i == len(arr):
        powerset.append(output)
    else:
        output_cpy  = list(output)
        power_set(arr, powerset, output_cpy, i+1)
        output.append(arr[i])
        output_cpy  = list(output)
        power_set(arr, powerset, output_cpy, i+1)

arr = [1,2,3,4,5]
powerset = [[]]
output = []
power_set(arr, powerset,output, 0)
powerset = powerset[1:]
for i in powerset:
    print(i)