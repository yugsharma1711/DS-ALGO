import math
def countpairs(arr, s):
    map = dict()
    pair=  0
    for i in arr:
        if s-i in map:
            pair += map[s-i]
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return pair

print(countpairs([1,1,1,1], 2))