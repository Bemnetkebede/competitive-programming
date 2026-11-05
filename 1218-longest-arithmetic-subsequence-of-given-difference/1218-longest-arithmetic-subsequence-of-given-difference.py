class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_val = 0
        for i in range(len(arr)):
            val = arr[i] - difference
            dp[arr[i]] = dp.get(val , 0) + 1
            max_val = max(max_val , dp[arr[i]])

        return max_val