class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def helper(n):
            if n == 0:
                return 0
            if n < 3:
                return 1
            return helper(n-1) + helper(n -2) + helper(n-3)
        return helper(n)
            
        