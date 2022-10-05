def stockSpan(arr):
    answer = []
    i = 0 
    while i != len(arr):
        buying_price = i
        selling_price = -1
        while i != len(arr)-1:
            if arr[i+1] >= arr[i]:
                i += 1
                selling_price = i
            else:
                break
        if buying_price <= selling_price:
            answer.append([buying_price, selling_price])
        i += 1
    return answer   
arr = [1,2,0,4,5]
print(stockSpan(arr))