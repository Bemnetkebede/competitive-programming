class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)
        m = len(mat[0])
        res = []
        i , j = 0 , 0
        direction = 1

        while len(res) < n*m:
            res.append(mat[i][j])
            if direction == 1:
                next_i = i- 1
                next_j = j + 1
                if 0 <= next_i < n and 0 < next_j < m:
                    i , j = next_i , next_j
                else:
                    if j + 1 < m:
                      j += 1
                    else:
                        i += 1
                    direction = -1
            else:
                next_i = i + 1
                next_j = j - 1                
                if 0 <= next_i < n and 0 <= next_j < m:
                   i, j = next_i, next_j
                else:
                    if i + 1 < n:
                        i += 1
                    else:
                        j += 1
                    direction = 1  
        return res
        