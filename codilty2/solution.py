# python code to count  how many first  elements are the same as the last element in S 
# check if the first and last char of s are the same
def countSame(s):
    count = 0
    N=len(s)

    for i in range(N):
        # check if the two elements are the same
        if s[0] == s[-1]:
            count += 1
            # planning of using slice method to remove the first element through slicing the second to the end
        s = s[1:] + s[0] 
    return count



    

