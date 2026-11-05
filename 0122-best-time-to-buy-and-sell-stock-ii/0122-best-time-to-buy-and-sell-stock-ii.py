class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        print(dp)
        for i in range(1, n):
            dp[i] = max(dp[i-1] + (prices[i] - prices[i-1]) , dp[i-1])
            # if prices[i] > prices[i-1]:
            #     dp[i] = dp[i-1] + (prices[i] - prices[i-1])
            # else:
            #    dp[i] = dp[i-1]
        return dp[-1]
            
        