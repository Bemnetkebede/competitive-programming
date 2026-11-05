class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        n = len(piles)
        l = 0
        r = n - 1 
        while l <= r:
            alice += max(piles[l] , piles[r])
            bob += min(piles[l] , piles[r])
            l += 1
            r -= 1 
        return alice > bob 
         

            
            
        