class Solution(object):
    def findMaxK(self, nums):
       nums.sort()
       seen = set(nums)
       l=0
       r = len(nums)-1
       while l < r:
            if nums[r] > 0 and - nums[r] in seen:
                return nums[r]
            else:
                r -= 1
       return -1
       
        
        