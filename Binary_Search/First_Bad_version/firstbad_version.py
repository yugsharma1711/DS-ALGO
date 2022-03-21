def firstbadVersion(start, end, badversion):
    if start > end:
        return badversion
    mid = start + end 
    mid = mid // 2
    if isBadVersion(mid):
        badversion = mid
        return firstbadVersion(start, mid-1, badversion)
    else:
        return firstbadVersion(mid + 1, end, badversion)