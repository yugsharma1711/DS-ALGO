from asyncio import current_task


def sum_sub(arr, s):
        curr_sum = 0
        start = 0
        if s== 0:
            return[-1]
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum > s:
                while curr_sum > s and start <= i:
                    curr_sum -= arr[start]
                    start += 1
            if curr_sum == s:
                return [start+1, i+1]
        return [-1]
arr = [1,2,3,7,4]
print(sum_sub(arr, -1))