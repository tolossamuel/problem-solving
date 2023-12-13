class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        def column(arr):
            if arr.count(1) == 1:
                return True
            else:
                return False
        def row(arr,x):
            count = 0
            for i in range(len(mat)):
                if arr[i][x] == 1:
                    count += 1
            if count ==1:
                return True
            else:
                return False
        ans  = 0
        for i in  range(len(mat)):
            for y in range(len(mat[0])):
                if mat[i][y]==1:
                    if column(mat[i]) and row(mat,y):
                        ans += 1
        return ans