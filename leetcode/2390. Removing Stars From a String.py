class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
                
            