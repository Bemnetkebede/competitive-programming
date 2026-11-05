class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        for i in grid:
           i.sort(reverse=True)
        
        res = []
        if k == 0:
            return 0
        for i in range(len(limits)  -1 , -1 , -1):
            x = limits[i]
            res.extend(grid[i][:x])
        res.sort()
        return sum(res[-k:])



        