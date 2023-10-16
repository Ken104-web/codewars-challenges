def solution(S):
    count = 0
    N = len(S)

    for i in range(N):
        if S[i] == 'X':
            count += 1
        elif  S[i + 1] == "." and S[i] == 'X':
            count +=1

    return count
