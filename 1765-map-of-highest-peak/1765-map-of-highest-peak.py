class Solution:
    def highestPeak(self, iswater: List[List[int]]) -> List[List[int]]:
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()
        visited = set()
        for i in range(len(iswater)):
            for j in range(len(iswater[0])):
                if iswater[i][j] == 1:
                    q.append((i,j))
                    iswater[i][j] = 0
                    visited.add((i,j))
        def inbound(r,c):
            return 0 <= r < len(iswater) and 0 <= c < len(iswater[0])
        while q:
            r, c = q.popleft()
            for dr , dc in direction:
                nr , nc = dr + r , dc + c
                if inbound(nr,nc) and (nr,nc) not in visited:
                    iswater[nr][nc] =  iswater[r][c] + 1
                    visited.add((nr , nc))
                    q.append((nr,nc))
        return iswater   

        
            

