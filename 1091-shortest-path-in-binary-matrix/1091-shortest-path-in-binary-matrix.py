class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(r , c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        direction =  [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
        visited = set((0, 0))
        q = deque([(0, 0, 1)])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        while q:
            r , c , l = q.popleft()
            if r == len(grid) - 1 and c == len(grid) - 1:
                return l
            for dr , dc in direction:
                nr , nc = dr + r,dc + c
                if inbound(nr , nc)  and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    q.append((nr , nc ,  l + 1))
                    visited.add((nr , nc))

        return -1
        
                