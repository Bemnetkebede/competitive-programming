class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        l , r = 0 ,len(nums) - 1
        max_pair_sum = 0 
        while l < r:
           sum = nums[l] + nums [r]
           max_pair_sum = max(max_pair_sum, sum)
           l += 1
           r -= 1
        return max_pair_sum 
        