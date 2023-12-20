class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        index = 0
        value = k
        while(value<len(s)):
            if index ==  0:
                s = s[value-1::-1] + s[value:]
                print(s)
                index += k*2
                value += k*2
            else:

                s = s[:index]+s[value-1:index-1:-1]+s[value:]
                index += k*2
                value += k*2
        if index < len(s):
            value = len(s)
            s = s[:index]+ s[value-1:index-1:-1] + s[value:]
        return s
        
            
        