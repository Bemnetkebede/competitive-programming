class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        direction  =  [[0,1], [1,0], [0,-1], [-1,0]] 
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i , j))
                    visited.add((i,j))
        def inbound(r, c):
            return 0 <= r <len(grid) and 0 <= c < len(grid[0])
        
        max_dis = 0
        print(len(grid) * len(grid[0]) , len(q))
        if len(grid) == 0 or len(q) == len(grid) * len(grid[0]):
            return -1
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                for dr , dc in direction:
                    nr , nc = dr + r , dc + c
                    if inbound(nr, nc) and (nr , nc) not in visited:
                            q.append((nr , nc))
                            visited.add((nr , nc))
            max_dis += 1
        return max_dis - 1

