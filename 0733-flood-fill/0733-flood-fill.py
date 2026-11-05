class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([([sr , sc],image[sr][sc] , color )])
        image[sr][sc] = color
        visited = set()
        direction  = [[0,1], [1,0], [0,-1], [-1,0]]
        def inbound(r , c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        while q:
            val ,ori , ch = q.popleft()
            sr , sc = val
            for r , c in direction:
                dr , dc = sr + r , sc + c
                if inbound(dr , dc) and image[dr][dc] == ori and (dr , dc) not in visited:
                       image[dr][dc] = color
                       q.append(([dr , dc] , ori , color))
                       visited.add((dr , dc))
               

        return image



        