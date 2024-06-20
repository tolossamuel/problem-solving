class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 1 if "1" in matrix[-1] else 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(len(matrix)-2,-1,-1):
            temp = 0
            for y in range(n-1,-1,-1):
                if y == (n-1):
                    if matrix[i][y] == "1":
                        ans = max(ans,1)
                else:
                    if matrix[i][y] != "0" and matrix[i][y+1] != "0" and matrix[i+1][y] != "0" and matrix[i+1][y+1] != "0":
                        
                        rec = min(int(matrix[i][y+1]),int(matrix[i+1][y+1]),int(matrix[i+1][y]))
                    
                        matrix[i][y] = str(int(matrix[i][y]) + rec)
                        
                        ans = max(ans,int(matrix[i][y]))
                    elif matrix[i][y] != "0":
                        ans = max(ans,int(matrix[i][y]))
          
        return ans**2
    
