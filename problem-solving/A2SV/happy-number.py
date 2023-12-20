class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
       
        def happy(n,dic):
            if len(str(n)) == 1:
                if n == 7 or n == 1:
                    return True
                else:
                    return False
            else:
                m = str(n)
                sumOf = 0
                for i in range(len(m)):
                    sumOf += int(m[i])**2
                
                
                
                return happy(sumOf,dic)
       
        ans = happy(n,{})
        
        return ans
        