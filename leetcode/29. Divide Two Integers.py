class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        div = (dividend//divisor)
        if (div < (-2**31)):
            return -2**31
        if (div < 0 and dividend%divisor != 0):
            return ((div)+1)
        if (div > (2**31 - 1)):
            return (2**31 - 1)
        
        
        return div

       
       