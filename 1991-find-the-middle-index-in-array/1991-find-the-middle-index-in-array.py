class Solution(object):
    def findMiddleIndex(self, nums):
        total = sum(nums)
        ls = 0
        for i in range(len(nums)):
            rs = total - ls 
            ls += nums[i]
            if ls == rs:
                return i
            
        return -1
            