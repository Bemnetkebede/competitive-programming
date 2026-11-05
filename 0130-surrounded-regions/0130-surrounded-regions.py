class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return board

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        visited = set()
        rows, cols = len(board), len(board[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        for i in range(rows):
            for j in [0, cols - 1]:
                if board[i][j] == 'O':
                    q.append((i, j))
                    visited.add((i, j))
        for j in range(cols):
            for i in [0, rows - 1]:
                if board[i][j] == 'O':
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            i, j = q.popleft()
            board[i][j] = 'T'
            for r, c in direction:
                dr, dc = r + i, c + j
                if inbound(dr, dc) and board[dr][dc] == 'O' and (dr, dc) not in visited:
                    q.append((dr, dc))
                    visited.add((dr, dc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        return board



                
       
        