class Solution(object):
    def majorityElement(self, nums):
       nums.sort()
       majority=nums[len(nums)//2]
       return majority
       