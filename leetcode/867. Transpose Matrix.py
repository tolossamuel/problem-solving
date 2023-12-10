class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        tMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for y in range(len(matrix[0])):
                tMatrix[y][i] = matrix[i][y]
        return tMatrix 