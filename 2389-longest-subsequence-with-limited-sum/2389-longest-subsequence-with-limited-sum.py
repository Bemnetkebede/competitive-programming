class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
    
        # Compute the prefix sum array
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        # Two-pointer approach to answer each query
        result = []
        for q in queries:
            l = 0
            r = 0
            while r < len(prefix_sum) and prefix_sum[r] <= q:
                r += 1
            result.append(r)  
        return result