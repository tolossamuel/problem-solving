class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for y in range(1,len(matrix[0])):
                matrix[i][y] += matrix[i][y-1]
        for y in range(1,len(matrix)):
            for i in range(len(matrix[0])):
                matrix[y][i] += matrix[y-1][i]
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans = (self.matrix [row2][col2])
        # print(ans)
        if row1 - 1 >= 0:
            ans -= self.matrix [row1-1][col2]
            # print(ans,self.matrix [row1-1][col1])
        if col1 -1 >= 0:
            ans -= self.matrix [row2][col1-1]
        if row1-1 >=0  and (col1-1 )>= 0:
            ans += self.matrix [row1-1][col1-1]
           
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)