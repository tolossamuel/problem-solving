class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        neg = 1
        if num < 0:
            num *= -1
            neg = -1
        s = list(str(num))
        
        s.sort()
        if neg == -1:
            s.reverse()
        i = 0
        while(s[i] == "0"):
            i+=1
            if i >= len(s):
                return num
            
        
        if i < len(s) and i != 0:
            s[0],s[i] = s[i],s[0]
        return (int("".join(s)) * neg)

