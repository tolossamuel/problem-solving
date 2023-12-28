class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        left = 0
        right = len(mat)-1
        ans = 0
        n = len(mat)-1
        if len(mat) == 1:
            return mat[0][0]
        for i in range(len(mat)//2):
            ans += mat[i][left]+ mat[i][right]
            ans += mat[n-i][left] + mat[n-i][right]
            left += 1
            right -= 1
        if left == right:
            ans += mat[n//2][left]
        return ans
            