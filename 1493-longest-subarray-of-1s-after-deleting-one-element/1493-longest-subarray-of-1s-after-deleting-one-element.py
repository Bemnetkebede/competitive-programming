class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        res = 0
        zero_count = 0
        for right in range(len(nums)):
            zero_count += 1 if nums[right] == 0 else 0
            while zero_count > 1 :
                zero_count -= 1 if nums[left] == 0 else 0
                left += 1
            res = max(res, right-left)
        return res
        