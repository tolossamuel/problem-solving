class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        stack = []
        for i in s:
            if i == " ":
                stack = []
            else:
                stack.append(i)
        return len(stack)