class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def checker(mid):
            balls = 1
            prev = position[0]
            for i in range(len(position)):
                cur_pos = position[i] - prev
                if cur_pos >= mid:
                    balls +=1 
                    prev = position[i]
            return balls >= m
        low = 1
        high = max(position) - min(position)
        while low <= high:
            mid = (low + high)//2
            if checker(mid):
                low = mid + 1
            else:
                 high = mid -1
        return high
        
        