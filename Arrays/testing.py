def minJump(arr):
    jumps = 0
    i=0
    while i < len(arr)-1:
            if arr[i] == 0:
                return False;
            curr_index = i
            last_index = i + arr[i]
            if last_index >= len(arr)-1:    
                jumps += 1
                i = last_index
            else:
                k=0
                j=last_index
                final_index = last_index
                while j > curr_index:
                    temp = arr[j] - k
                    if temp > arr[final_index]:
                        final_index = j
                    k += 1
                    j-=1
                i = final_index
                jumps += 1
    return jumps
    
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
minJump(arr)