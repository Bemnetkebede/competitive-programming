class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        l = 2**n - 1
        md = l // 2 + 1
        if n == 1: return '0'
        if k == md:
            return '1'
        elif k < md:
             return self.findKthBit(n-1 , k)
        else:
            return '1' if self.findKthBit(n-1 , l-k+1) == '0' else '0'




        