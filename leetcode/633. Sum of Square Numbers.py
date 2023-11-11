class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        right = c
        if (c > 4):
            right = int(math.sqrt(c))
        # print(right)
        for i in range(right+1):
            if (i*i <= c):

                left = int((c - (i*i))**0.5)
                # print(left)
                if ((left*left) + (i*i) )== c:

                    return True
        return False