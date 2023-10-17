# total value of rolls  = mean(4) * total number of known rolls(N) plus forgo
# number of rolls = N  + missing rolls(F) N + F = dice rolled
# sum if dice rolled = (N + F) * M(mean)
# N dice told eg= [3, 2, 4, 3] number of rolls = 4
# F dice not told
# meaning that if we subtracted sum of array A or N from total value of rolls we get F(missing) 
def solution(A, F, M):
    N = len(A)
    total_value_rolls = M * (N + F)
    total_sum_known = sum(A)
    left = total_value_rolls - total_sum_known

  
    
    