class NumMatrix:
    def inbound(self , row:int ,col:int)->bool:
        return 0 <= row < self.row and 0 <= col < self.col
    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefix = [[0] * self.col for _ in range(self.row)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.prefix[i][j] = matrix[i][j]
                if self.inbound(i-1 , j):
                    self.prefix[i][j] += self.prefix[i-1][j]
                if self.inbound(i , j-1):
                    self.prefix[i][j] += self.prefix[i][j-1] 
                if self.inbound(i-1, j-1):
                   self.prefix[i][j] -= self.prefix[i-1][j-1]
        print(self.prefix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       
        ans = self.prefix[row2][col2] 
        if col1 > 0: 
           ans -= self.prefix[row2][col1-1]
        if row1 > 0:
           ans -= self.prefix[row1-1][col2]    
        if row1 > 0 and col1 > 0:
           ans += self.prefix[row1-1][col1-1]
        return ans

            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)