class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(mid):
            cnt = 1
            cur_sum = 0
            for i , num in enumerate(weights):
                cur_sum += num
                if cur_sum  > mid:
                    cnt += 1
                    cur_sum = num
            return cnt <= days
        
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high) // 2
            if isFeasible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low



                  

        