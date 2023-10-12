class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def palindrom(n,x):
            pa = []
            while(n != 0):
                pa.insert(0,str(n%x))
                n //=2
            pa = "".join(pa)
            if pa[0:]==pa[::-1]:
                return True
            else:
                return False
        for i in range(2,(n-2)+1,+1):
            if not(palindrom(n,i)):
                return False
        return True