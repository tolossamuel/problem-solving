class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        n = ""
        for i in range(len(s)):
         
            if (s[i].isalnum()):
                n+= s[i].lower()
            

        if n == n[::-1]:
            return True
        else:
            return False
            

       
        