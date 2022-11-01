def firstNonRepeating(arr):
    _dict = ()
    for i in arr:
        if i in _dict:
            _dict[i] += 1
        else:
            _dict[i] = 1
    for i in arr:
        if _dict[i] == 1:
            return i
    return 0