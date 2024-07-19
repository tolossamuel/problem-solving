class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = [float("inf")]*len(matrix)
        col = [float("-inf")]*len(matrix[0])
        for i in range(len(matrix)):
            for y in range(len(matrix[0])):
                col[y] = max(col[y],matrix[i][y])
                row[i] = min(row[i],matrix[i][y])
       
        dic = Counter(col)
        ans = []
        for x in row:
            if x in dic and dic[x] > 0:
                ans.append(x)
                dic[x] -= 1
        
        return ans