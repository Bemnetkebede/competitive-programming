class Solution(object):
    def findTheArrayConcVal(self, nums):
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
           concat =  int(str(nums[l]) + str(nums[r]))
           res += concat
           l += 1
           r -= 1
        if l == r:
            res += nums[l]
        return res
        
        