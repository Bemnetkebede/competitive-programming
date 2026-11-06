class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        if n > 1:
            x = self.fac(n)
            while x % 10 == 0:
                cnt += 1
                x //= 10
        return cnt
    def fac(self , n:int)->int:
        if n==1: return 1
        c = n * self.fac(n-1)
        return c
        
        
        
        
        