class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def mod_pow(base:int , exp : int) ->int:
            if exp == 0:
                return 1 
            half =mod_pow(base, exp // 2)
            res = (half * half) % MOD
            if exp % 2 == 1:
                res = (res * base) % MOD
            return res

            
        Even_Cnt = (n + 1) // 2  
        Odd_cnt = n // 2  
        return (mod_pow(5,Even_Cnt) * mod_pow(4,Odd_cnt)) % MOD


 