arr_1 = [1,2,3,4]
arr_2 = [1,2,3]
num_1 = 0
num_2 = 0
count = 1
for i in range(len(arr_1)-1, -1, -1):
    num_1 += arr_1[i] * count
    count *= 10
count = 1
for i in range(len(arr_2) - 1, -1, -1):
    num_2 += arr_2[i] * count
    count *= 10
print(num_1 + num_2)