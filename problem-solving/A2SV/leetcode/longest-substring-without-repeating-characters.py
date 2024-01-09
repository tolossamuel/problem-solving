class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = set()
        left = 0
        counter = 0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[left])
                left += 1
            char.add(s[i])
            counter = max(counter, i-left+1)
        return counter