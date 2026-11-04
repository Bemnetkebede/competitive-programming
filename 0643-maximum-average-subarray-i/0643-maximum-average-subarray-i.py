class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_res = window_sum
        for i in range(1 , len(nums) - k + 1):
            window_sum -= nums[i - 1]
            window_sum += nums[i + k - 1]
            
            max_res = max(window_sum , max_res)
        print(max_res)
        return max_res/k

