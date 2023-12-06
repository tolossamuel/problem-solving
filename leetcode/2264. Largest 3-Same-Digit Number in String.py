class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = 1
        ans = 0
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                n += 1
            elif n >=3:
                ans = max(ans , num[i-1])
                n = 1
            else:
                n = 1
        else:
            if n >=3:
                ans = max(ans , num[i-1])
                
        if ans == 0:
            return ""
        string = ans+ans+ans
        return string
            