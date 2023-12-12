# find the  two largest numbers of the  input array 
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        r = 0
        current_max = nums[0]

        for i in range(1, len(nums)):
            r = max(r, (current_max - 1) * (nums[i] - 1))
            current_max = max(current_max, nums[i])
        
        return r