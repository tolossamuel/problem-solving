class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans  = 0
        while(n > 1):
            
            if n%2 != 0:
                n += 1
                ans -= 1
            n /= 2
            ans += n
            print(ans,n)
        return ans