class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1) 
        for i in range(n-1, -1, -1):
            pt, br = questions[i]
            take = pt
            if i + br + 1 <= n:
                take += dp[i + br + 1]
            skip = dp[i+1]
            dp[i] = max(take, skip)

        return dp[0]