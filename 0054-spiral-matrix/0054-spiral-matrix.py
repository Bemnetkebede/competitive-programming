class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        t , l , r , b = 0 , 0 , n-1 , m-1
        print(b)
        res = []
        while l <= r and t <= b:
            # print(l, r, t, b)
            for i in range(l , r+1):
                res.append(matrix[t][i])
            t += 1
            # print(res,t , b)
            for j in range(t , b + 1):
                res.append(matrix[j][r])
            r -= 1
            
            if t <= b:
                for y in range(r, l - 1, -1):
                    res.append(matrix[b][y])
                b -= 1
            if l <= r:
                for k in range(b, t - 1, -1):
                    res.append(matrix[k][l])
                l += 1  
        return res

        # for i in range(m):
        #     for j in range(n):
        #         res.append(matrix[i][j])
        #         # if j != m-1:
        #         #    res.append(matrix[i][j])
        #         if j == m-1:
        #             # res.append(matrix[i+1][j])
        #             i += 1
        #         elif i == n - 1:
        #             # res.append(matrix[i+1][j])
        #             j -= 1
        #         elif j == 0:
        #             i += 1
        #         elif i == 1:
        #             i += 1
        #             j += 1
        # return res




            

        