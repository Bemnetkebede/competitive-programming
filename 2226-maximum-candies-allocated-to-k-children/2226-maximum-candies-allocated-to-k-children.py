class Solution(object):
    def maximumCandies(self, candies, k):
        candies.sort()
        def checker(mid):
            ppl = 0
            for i in range(len(candies)):
                ppl += candies[i]//mid
            return ppl >= k
          
        low = 1
        high = max(candies)
        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                low = mid + 1   
            else:
                high = mid - 1
        return high 