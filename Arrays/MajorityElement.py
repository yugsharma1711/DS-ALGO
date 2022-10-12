def majorElement(A, N):
        A.sort()
        counter = 0
        if N == 1:
            return A[0]
        for i in range(N//2):
            if A[counter + N//2] == A[i]:
                return A[i]
            counter += 1
        return -1