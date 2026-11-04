class Solution(object):
    def rotate(self, matrix):
        l , r = 0 , len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top , bottom = l , r
                topleft = matrix[top][l + i]

                #move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l] 
                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move left top to top right top
                matrix[top + i][r] = topleft
            l += 1
            r -= 1
        print(matrix)
                  