class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum , max_sum = 0 , 0
        cur_sum = 0
        mx = 0
        res = 0
        for num in nums:
            cur_sum += num
            mx = max(abs(cur_sum - min_sum), abs(cur_sum - max_sum))
            res = max(res ,mx)
            min_sum = min(min_sum , cur_sum)
            max_sum = max(max_sum , cur_sum)
        return res
        
