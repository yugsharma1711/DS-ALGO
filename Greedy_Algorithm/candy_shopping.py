def candyStore(candy,N,k):
        candy.sort()
        cost = 0
        low = 0
        high = len(candy) - 1
        while low <= high:
            cost += candy[low]
            for i in range(k):
                high-=1
            low += 1
        _cost = 0
        low = 0
        high = len(candy)-1
        candy.reverse()
        while low <= high:
            _cost += candy[low]
            for i in range(k):
                high-=1
            low += 1
        return [cost, _cost]
