class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        left_col = len(matrix[0])-1
        right_row = len(matrix)-1
        pos = 0
        while(left_row <= right_row):
            mid = (left_row + right_row)//2
            if matrix[mid][left_col] >= target:
                pos = mid
                right_row = mid - 1
            else:
                left_row = mid + 1
        left = 0
        right = len(matrix[0])-1
        while(left <= right):
            mid =  (left + right)//2
            if matrix[pos][mid] == target:
                return True
            elif matrix[pos][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False 