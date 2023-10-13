def solution(A):
    count = 0
    filled_countries = set()
    for i in A:
        i = tuple.add(i)
        if i not in filled_countries:
            count += 1
            filled_countries.add(i)
        return count