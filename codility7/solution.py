def solution(S):
    count = 0
    N = len(S)

    for i in range(N):
        if S[i] == 'X':
            count += 1
        elif i + 1 < N and S[i + 1] == "." and S[i] == 'X':
            count +=1
    return count 

# def solution(S):
#     count = 0
#     N = len(S)
#     i = 0
#     while i < N:   
#          if S[i] == "X":
#             count +=1
#             i += 2
#          else: i+=1
#     return count

