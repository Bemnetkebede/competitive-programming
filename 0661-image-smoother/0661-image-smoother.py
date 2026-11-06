class Solution(object):
    def imageSmoother(self, img):
        row = len(img)
        col = len(img[0])
        res = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                total = 0
                count = 0
                for i in range(r  - 1 , r + 2):
                    for j in range(c - 1 , c + 2):
                        if i < 0 or i == row or j < 0 or j == col:
                            continue
                        total += img[i][j]
                        count += 1
                res[r][c] = total//count
        return res

        