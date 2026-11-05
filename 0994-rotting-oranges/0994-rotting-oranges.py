class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction =  [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()
        q = deque()
        cnt = 0
        fresh = 0
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direction:
                    nr , nc = dr + r , dc + c
                    if inbound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        grid[nr][nc] = 2
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh -= 1
            cnt += 1
        return cnt if fresh == 0 else -1
            
                    






        