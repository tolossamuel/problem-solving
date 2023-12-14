class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            temp = self.helper(s,i,i)
            if len(temp) > len(ans):
                ans = temp
            temp = self.helper(s,i,i+1)
            if len(temp) > len(ans):
                ans = temp
        return ans
    def helper(self,s,l,r):
        while(l>=0 and r< len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return (s[l+1:r])
