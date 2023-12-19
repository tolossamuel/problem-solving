class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            for y in range(len(matrix[0])):
                if i+1 < len(matrix)  and y+1 < len(matrix[0]):
                    if matrix[i][y] != matrix[i+1][y+1]:
                        return False
        return True
                