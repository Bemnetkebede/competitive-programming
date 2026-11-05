class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction =  [[0,1], [1,0], [0,-1], [-1,0]] 
        q = deque([(entrance[0], entrance[1],0)])
        # print(q)
        visited = set()
        distance = 0
        def inbound(r,c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])
        def checker(r , c):
            return r == 0 or c == 0 or r == (len(maze) -1) or c == (len(maze[0])-1)
        while q:
            r,c,d = q.popleft()
            # r,c = pos
            # print(pos , d)
            # visited.add((r , c))
            
            if checker(r,c) and maze[r][c] == '.' and [r,c] != entrance:
                return d
            for x, y in direction:
                dr , dc = r+x , c+y
                if inbound(dr,dc) and maze[dr][dc] != '+' and (dr,dc) not in visited:
                    visited.add((dr , dc))
                    q.append((dr,dc,d+1))
                    # distance += 1
        return -1    
                    



        