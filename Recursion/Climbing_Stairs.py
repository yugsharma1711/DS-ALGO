def ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    ans = ways(n-1) + ways(n-2)
    return ans
print(ways(3))