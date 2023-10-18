def solution(S):
    N = len(S)
    frequency = [0] * 26

    for i in range(N):
        frequency[ord(S[i]) - ord("a")]+= 1

    count = 0
    for i in range(len(frequency)):
        if frequency[i] % 2 == 1:
            count += 1
    
    return count

        

        

# def solution(S):    
#     if S.count('A') == len(S) or S.count('B') == len(S):       
#          return 0    
#     elif S[0] == 'B':        
#         S = S.replace('B', '', 1)    
#     elif S[-1] == 'A':           
#      S = S.replace('A', '', 1)    
#     else:        
#      first_A = S.index('A')        
#      last_A = S.rindex('A')        
#      S = S[first_A:last_A+1]        
#      return S.count('B')

