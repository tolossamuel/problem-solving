class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pref = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        # pref[0][0] = matrix[0][0]
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                pref[i][j] = matrix[i-1][j-1] + pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1]
        counter = 0
        
        for i in range(len(matrix)+1):
            for y in range(len(matrix[0])+1):
                for x in range(i):
                    for z in range(y):
                        temp = pref[i][y] - pref[i][z] - pref[x][y]
                        temp += pref[x][z]
                        if temp == target:
                            counter += 1
                        
                # print("========")
        return counter
                        

