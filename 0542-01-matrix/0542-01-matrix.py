class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        direction = [[0,1], [1,0], [0,-1], [-1,0]] 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                else:
                    mat[i][j] = float('inf')
        def inbound(r, c):
            return 0 <= r <len(mat) and 0 <= c < len(mat[0])
        while q:
            dis = 0
            r , c = q.popleft()
            for dr , dc in direction:
                nr , nc = dr + r , dc + c
                # if inbound(nr , nc) and (nr , nc ) not in visited:
                if inbound(nr , nc) and mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr , nc))
                    # if mat[nr][nc] == 0:
                    #     mat[r][c] = dis + 1
                    #     q.append((nr,nc))
                    #     visited.add((nr, nc))
                    # else:
                    #     dis += 1
        return mat


        