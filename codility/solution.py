#   A = [N, N, N]. Amplitude A = max{A[P] - A[Q] : 0 <= p, Q < N}
def solution(A):
    # initialize the max and min value with the FIRST element
    max_in_value = A[0]
    min_in_value = A[0]
# loop through A to updated the max_in_value and min_in_value if encountered
    for i in A:
        if i > max_in_value:
            max_in_value = i
        elif i < min_in_value:
            min_in_value = i
# if the element is single return 0
        elif len(A) == 0:
            return 0
    # calculation
    amplitude = max_in_value - min_in_value
    return amplitude