class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0:1}
        cur_sum = 0
        cnt = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - goal in prefix:
                cnt += prefix[cur_sum - goal]
            prefix[cur_sum] = prefix.get(cur_sum , 0) + 1
        return cnt
        
        