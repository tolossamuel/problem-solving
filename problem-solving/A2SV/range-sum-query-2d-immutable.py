class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for y in range(1,len(matrix[0])+1):
                self.pref[i][y] = matrix[i-1][y-1] + self.pref[i][y-1] + self.pref[i-1][y] - self.pref[i-1][y-1] 

        # for i in self.pref:
        #     print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(row1,col1,row2,col2)
        # print(self.pref[row2+1][col2+1],self.pref[row1][col2+1] , self.pref[row2+1][col1] , self.pref[row1][col1])
        return (self.pref[row2+1][col2+1] - self.pref[row1][col2+1] - self.pref[row2+1][col1] + self.pref[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)