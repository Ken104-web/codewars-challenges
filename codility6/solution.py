def solution(A):
    N = len(A)

    for i in range(N):
        num = A[i]
        count = 0
        # use linear search
        for j in range(N):
            if A[j] == num:
                count += 1
        if count == 1:
            return num
    return -1
        
