class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        left = 0
        right = len(mat)-1
        ans = 0
        for i in range(len(mat)):
            if i< len(mat)//2:
                if left == right:

                    ans += mat[i][left]
                    left -= 1
                    right += 1
                elif left + 1 == right:
                    ans += mat[i][left]+mat[i][right] 
                else:
                    ans += mat[i][left]+mat[i][right]
                    left += 1
                    right -= 1
            else:
                if left == right:
                    ans += mat[i][left]
                else:
                    ans += mat[i][left] + mat[i][right]
                left -= 1
                right += 1
        return ans
            