class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a,b = 0,1
        for i in range(n):
            a,b = b, a+b
        return a