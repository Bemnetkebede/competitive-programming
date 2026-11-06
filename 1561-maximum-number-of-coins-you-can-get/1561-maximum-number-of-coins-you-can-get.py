class Solution(object):
    def maxCoins(self, piles):
        n = len(piles)
        piles.sort(reverse = True)
        sum_ = 0
        for i in range(1,n-n//3,2):
            sum_ += piles[i]
        return sum_

            

        