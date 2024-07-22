class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for i in range(len(matrix)-2,-1,-1):
            
            for y in range(len(matrix[0])-1,-1,-1):
                if y +1 == len(matrix[0]):
                    matrix[i][y] += min(matrix[i+1][y],matrix[i+1][y-1])
                elif y -1 < 0:
                    matrix[i][y] += min(matrix[i+1][y],matrix[i+1][y+1])
                else:
                    matrix[i][y] += min(matrix[i+1][y],matrix[i+1][y+1],matrix[i+1][y-1])
        return min(matrix[0])