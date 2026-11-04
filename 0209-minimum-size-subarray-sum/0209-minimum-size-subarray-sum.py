class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        sum_sub = 0
        i = 0
        j = 0
        while j < len(nums) or sum_sub >= target:
            print(sum_sub)
            if sum_sub >= target:
                min_len = min(min_len , j - i )
                sum_sub -= nums[i]
                i += 1
                print('here we go' , min_len)
            else:
                sum_sub += nums[j]
                j += 1
        return 0 if min_len == float('inf') else min_len

