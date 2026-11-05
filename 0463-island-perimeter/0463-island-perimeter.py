class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0,1) , (0 , -1 ) , (1 , 0 ) , (-1 , 0)]
        def inbound(row, col):
             return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        p = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for dr , dc in direction:
                        nr , nc = row + dr , col+ dc
                        if not inbound(nr, nc) or grid[nr][nc] == 0: 
                            p += 1
        return p
                        


                    
                

                    


        