class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)-1,-1,-1):
          if num[i] in {"1","3","5","9","7"}:
            return num[:i+1]
        return ""