def sqrtN(n):
    ans = 0
    if n == 1:
        return n
    return find_sqrt(n, 0, n-1, ans)
def find_sqrt(num, start, end, ans):
    if start > end:
        return ans
    mid = start + end 
    mid = mid // 2
    mid_sq = mid * mid 
    if mid_sq > num:
        return find_sqrt(num , start, mid-1, ans)
    elif mid_sq < num:
        ans = mid
        return find_sqrt(num , mid+1 , end, ans)
    else:
        ans = mid
        return ans
print(sqrtN(105554))