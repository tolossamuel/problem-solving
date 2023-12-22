class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c=len(matrix)
        for i in range(c):
            for j in range(i,c):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(c):
            matrix[i]=matrix[i][::-1]
        




                    