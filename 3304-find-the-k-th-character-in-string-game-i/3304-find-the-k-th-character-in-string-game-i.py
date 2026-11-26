class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(k):
            if k == 1:
                return 0
            n = 0
            while 2 ** (n+1) < k:
                n += 1
            half =  2 ** n  
            return 1 + helper(k - half)
        return chr(ord('a') + helper(k))
