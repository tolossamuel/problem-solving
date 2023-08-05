class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,colum = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*(colum +1) for r in range(row+1)]
        
        for r in range(row):
            summ = 0
            for c in range(colum):
                summ += matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = summ + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        sumOfRegion = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1-1]
        top_left = self.sumMatrix[row1-1][col1-1]
        sumOfRegion -= (left - top_left + above)
        return sumOfRegion


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)