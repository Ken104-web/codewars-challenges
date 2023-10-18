
def solution(S):
    N = len(S)
    max_sum = 0

    for i in range(N):
        combined_values = int(S[i] + S[i + 1])
        combined_values2 = int(S[i] + S[i + 1])

        max_result = combined_values + combined_values2

        if max_result > max_sum:
            max_sum = max_result

    return max_sum


