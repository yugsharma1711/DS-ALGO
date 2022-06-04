def power_set(arr, powerset, i):
    if i == len(arr):
        return
    else:
        for j in range(len(powerset)):
            sample_set = list(powerset[j])
            sample_set.append(arr[i])
            powerset.append(sample_set)
        print(powerset)
        power_set(arr, powerset,i+1)


arr = [1,2,3,4]
powerset = [[]]
power_set(arr, powerset, 0)