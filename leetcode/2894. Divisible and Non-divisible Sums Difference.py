class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        x = 0
        y = 0
        for i in range(1,n+1,+1):
            if i%m == 0:
                x += i
            else:
                y += i
        return (y-x)
