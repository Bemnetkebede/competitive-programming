class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[ [grid[j][i], 0] for i in range(len(grid[0]))] for j in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                  org_val, su = dp[i][j]
                  if i == 0 and j == 0:
                    dp[i][j][1] = org_val
                  else:  
                    top = dp[i-1][j][1] if i > 0 else float('inf')
                    left = dp[i][j-1][1] if j > 0 else float('inf')
                    dp[i][j][1] = org_val + min(top, left)

        return dp[m-1][n-1][1]        