from itertools import count


def conscutiveInteger(arr):
    arr.sort()
    _dict = dict()
    counter = 0
    max_counter = 0
    for i in arr:
        if i in _dict:
            continue
        else:
            _dict[i] = 1
            if i-1 in _dict:
                counter += 1
            else:
                if max_counter < counter:
                    max_counter = counter
                counter = 0
    return max_counter+1

arr = [8,8,9,3,4]
print(conscutiveInteger(arr))