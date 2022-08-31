def findClosestElements(arr, k, x):
        for i in range(len(arr)):
            arr[i] -= x
        arr = sorted(arr, key = lambda x : abs(x))
        arr = arr[:k]
        for i in range(len(arr)):
            arr[i] += x
        arr.sort()
        return arr
