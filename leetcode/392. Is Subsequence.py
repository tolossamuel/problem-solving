class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        right = 0
        counter = 0
        for i in range(len(t)):
            if right < len(s):
                if s[right] == t[i]:
                    right += 1
                    counter += 1
            else:
                break
        if counter == len(s):
            return True
        else:
            return False