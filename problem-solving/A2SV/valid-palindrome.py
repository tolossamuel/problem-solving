class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        left = 0
        right = len(s) -1
        while(left < right):
            if not s[right].isalnum():
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif s[right].lower() == s[left].lower():
                left +=1
                right -= 1
            else:
                return False
        return True