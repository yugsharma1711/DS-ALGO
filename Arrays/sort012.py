def sort012(arr):
        n= len(arr)
        start=0 
        end = n-1
        while start < end:
            if arr[end] == 0 and (arr[start] == 2 or arr[start] == 1):
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1 
            if arr[start] == 0:
                start += 1
            if arr[end] == 2 or arr[end] == 1:
                end-=1
        start = 0
        end = n-1
        while  start < n and arr[start] == 0:
            start +=1
        while start < end:
            if arr[start] == 2 and arr[end] == 1:
                arr[start], arr[end] = arr[end], arr[start]
            if arr[start] == 1:
                start += 1
            if arr[end] == 2:
                end -= 1
        return arr

print(sort012([0,1]))