class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = [-1] * (n + 1)
        # def helper(n , sm):
        #     if n <= 2:
        #         return n
        #     if memo[n] != -1:
        #        return memo[n]
        #     memo[n] = helper(n-1 , memo) + helper(n-2 , memo)
        #     return memo[n]
        # return helper(n , memo)
        memo = [0] * (n + 1)
        memo[n] = 1
        memo[n-1] = 1
        for i in range(n - 2, -1, -1):
            memo[i] = memo[i+1] + memo[i + 2]
        return memo[0]

            
        
        