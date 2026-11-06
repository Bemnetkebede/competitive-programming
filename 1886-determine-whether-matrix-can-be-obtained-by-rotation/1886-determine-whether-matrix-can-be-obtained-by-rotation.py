class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)
        for _ in range(4):
            rotated = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    rotated[c][n-1-r] = mat[r][c]
            if rotated == target:
                return True
            mat = rotated
        return False