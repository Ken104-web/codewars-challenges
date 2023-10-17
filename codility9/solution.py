# total value of rolls  = mean(4) * total number of known rolls(N) plus F
# number of rolls = N  + missing rolls(F) N + F = dice rolled
# sum if dice rolled = (N + F) * M(mean)
# N dice told eg= [3, 2, 4, 3] number of rolls = 4
# F dice not told
# meaning that if we subtracted sum of array A or N from total value of rolls we get F(missing)
# so [3, 2, 4, 3] = 12 from total value = 24 we 12 which is F
# so find values of F 
def solution(A, F, M):
    N = len(A)
    total_value_rolls = M * (N + F)
    total_sum_known = sum(A)
    left = total_value_rolls - total_sum_known

    # if eg: value of F ==  17 and F = 2
    # 17/2 not possible since highest number in dice is 6  
    if left <= 0 or left < F:
        return [0]
    
    result = []
    while left:
        dice = min(left - F + 1, 6)
        result.append(dice)
        # update left
        left -= dice
        # dice values remaining
        F -= 1

    return result
    
    
    