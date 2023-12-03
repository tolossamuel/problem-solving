class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = ["a","e","i","o","u"]
        sumOf = 0
        for i in range(k):
            if s[i] in dic:
                sumOf += 1
        ans = sumOf
        for i in range(k,len(s)):
            if s[i-k] in dic:
                sumOf -= 1
            if s[i] in dic:
                sumOf += 1
            ans = max(ans,sumOf)
        return ans
    