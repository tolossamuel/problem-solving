class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        arr = [0] * (len(matrix[0])+1)
        ans = float("-inf")
        for row in matrix:
            for i in range(len(matrix[0])):
                arr[i] = arr[i] + 1 if row[i] == "1" else 0
            stack = []
            for i in range(len(arr)):
                while stack and arr[i] < arr[stack[-1]]:
                    h = arr[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        
        return ans if ans != float("-inf") else 0   