class Solution:
    def numSquares(self, n: int) -> int:
        val = []
        for i in range(1,n + 1):
            if math.isqrt(i) ** 2 == i:
                val.append(i)
        dp = [float('inf')] * ( n + 1 )
        dp[0] = 0
        for i in range(1 , n+1):
             for square in val:
                if square <= i:
                  dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]