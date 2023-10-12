def solution(K, A):
        N = len(A)
        count = 0
        for i in range(N):
            minimum=A[i]
            maximum=A[i]
            for x in range(i, N):
               maximum = max(maximum, A[x])
               minimum = min(minimum, A[x])
               if maximum - minimum <= K:
                count += 1
        return count