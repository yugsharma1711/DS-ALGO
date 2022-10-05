def firstRepeated(arr):
        pairs = []
        map = dict()
        for i in range(len(arr)):
            if arr[i] in map:
                pairs.append(map[arr[i]])
            else:
                map[arr[i]] = (arr[i], i)
        pairs = sorted(pairs, key = lambda x: x[1])
        if len(pairs) == 0:
            return -1
        return pairs[0][1] + 1 

print(firstRepeated([1,4,5,3,3,5]))