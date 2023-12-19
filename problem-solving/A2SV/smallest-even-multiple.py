class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 2
        commen = n*2
        while((commen/min(2,n)) %2 ==0 and commen/min(2,n) %n ==0):
            commen /= min(2,n)
        return commen
        